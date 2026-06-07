import feedparser
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from email.utils import parsedate_to_datetime

from src.utils.logger import logger
from src.config.settings import RSS_FEEDS
from src.database.db import get_session_context
from src.models.models import Article
from src.categorization.categorizer import categorize_article

def extract_article_content(url: str) -> str:
    """
    Visits the article URL and extracts the readable text content.

    Args:
        url (str): The URL of the article.

    Returns:
        str: The extracted text content or empty string on failure.
    """
    try:
        # A common User-Agent to avoid being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text from paragraphs as a simple heuristic for article content
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text(strip=True) for p in paragraphs])

        return content
    except Exception as e:
        logger.error(f"Failed to extract content from {url}: {e}")
        return ""

def parse_published_date(date_str: str) -> datetime:
    """Parses standard RSS date strings into datetime objects."""
    try:
        if not date_str:
            return datetime.utcnow()
        # Handle parsedate parsing
        dt = parsedate_to_datetime(date_str)
        return dt.replace(tzinfo=None) # Strip timezone for SQLite
    except Exception:
        return datetime.utcnow()

def collect_articles():
    """
    Main workflow to collect articles from all configured RSS feeds.
    Reads feed, extracts metadata, fetches content, categorizes, and stores.
    """
    logger.info("Collection start")
    articles_collected = 0

    with get_session_context() as session:
        for feed_config in RSS_FEEDS:
            source_name = feed_config['name']
            feed_url = feed_config['url']

            logger.info(f"Processing feed: {source_name} ({feed_url})")

            try:
                feed = feedparser.parse(feed_url)

                if feed.bozo and hasattr(feed, 'bozo_exception'):
                    logger.warning(f"Feed parser issue for {source_name}: {feed.bozo_exception}")
                    # Try to continue despite bozo exceptions, as some feeds are just malformed slightly

                for entry in feed.entries:
                    title = entry.get('title', '')
                    url = entry.get('link', '')
                    published_date_str = entry.get('published', entry.get('updated', ''))

                    if not url or not title:
                        continue

                    # Check if article already exists
                    existing_article = session.query(Article).filter_by(url=url).first()
                    if existing_article:
                        continue # Skip existing URLs

                    published_date = parse_published_date(published_date_str)

                    # Fetch content
                    content = extract_article_content(url)

                    # Categorize
                    category = categorize_article(title, content)

                    # Create article
                    new_article = Article(
                        title=title,
                        source=source_name,
                        url=url,
                        published_date=published_date,
                        content=content,
                        category=category
                    )

                    session.add(new_article)
                    articles_collected += 1

                # Commit after each feed to save partial progress
                session.commit()

            except Exception as e:
                logger.error(f"Error processing feed {source_name}: {e}")
                session.rollback()

    logger.info(f"Collection finish. Number of articles collected: {articles_collected}")
    return articles_collected

if __name__ == "__main__":
    # For testing the collector manually
    from src.database.db import init_db
    init_db()
    collect_articles()
