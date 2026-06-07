import re
from src.config.settings import CATEGORY_KEYWORDS

def categorize_article(title: str, content: str) -> str:
    """
    Categorizes an article based on keyword mapping defined in configuration.

    Args:
        title (str): The title of the article.
        content (str): The content/body of the article.

    Returns:
        str: The assigned category.
    """
    combined_text = f"{title} {content}".lower()

    # Iterate through categories and check for keyword matches
    for category, keywords in CATEGORY_KEYWORDS.items():
        if category == "Other":
            continue # Handle 'Other' as a fallback

        for keyword in keywords:
            # Look for keyword as a whole word
            pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
            if re.search(pattern, combined_text):
                return category

    return "Other"
