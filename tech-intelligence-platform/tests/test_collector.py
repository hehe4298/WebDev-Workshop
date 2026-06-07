import pytest
from unittest.mock import patch, MagicMock
from src.collectors.rss_collector import collect_articles, extract_article_content, parse_published_date
from src.models.models import Article

@patch('src.collectors.rss_collector.requests.get')
def test_extract_article_content_success(mock_get):
    mock_response = MagicMock()
    mock_response.content = b"<html><body><p>Test paragraph 1.</p><p>Test paragraph 2.</p></body></html>"
    mock_get.return_value = mock_response

    content = extract_article_content("http://test.com")
    assert content == "Test paragraph 1. Test paragraph 2."

@patch('src.collectors.rss_collector.requests.get')
def test_extract_article_content_failure(mock_get):
    mock_get.side_effect = Exception("Connection error")
    content = extract_article_content("http://test.com")
    assert content == ""

def test_parse_published_date():
    dt = parse_published_date("Mon, 01 Jan 2024 12:00:00 GMT")
    assert dt is not None
    assert dt.year == 2024

    dt_invalid = parse_published_date("invalid date")
    assert dt_invalid is not None # returns current time

@patch('src.collectors.rss_collector.feedparser.parse')
@patch('src.collectors.rss_collector.extract_article_content')
def test_collect_articles(mock_extract, mock_feedparser, test_session):
    mock_extract.return_value = "Mocked article content about AI"

    # Mock the feed
    mock_feed = MagicMock()
    mock_feed.bozo = False
    mock_feed.entries = [
        {
            "title": "Test AI Article",
            "link": "http://test.com/article1",
            "published": "Mon, 01 Jan 2024 12:00:00 GMT"
        }
    ]
    mock_feedparser.return_value = mock_feed

    # Run collection with mocked feeds but actual DB (which is mocked by conftest)
    with patch('src.collectors.rss_collector.RSS_FEEDS', [{"name": "Test Feed", "url": "http://test.feed"}]):
        collected = collect_articles()

    assert collected == 1

    # Verify in DB
    article = test_session.query(Article).first()
    assert article is not None
    assert article.title == "Test AI Article"
    assert article.category == "AI"

    # Test duplicate prevention
    with patch('src.collectors.rss_collector.RSS_FEEDS', [{"name": "Test Feed", "url": "http://test.feed"}]):
        collected_again = collect_articles()

    assert collected_again == 0 # Should skip duplicate
