# Configuration for RSS feeds
RSS_FEEDS = [
    {
        "name": "Reuters Technology",
        "url": "http://feeds.reuters.com/reuters/technologyNews"
    },
    {
        "name": "TechCrunch",
        "url": "https://techcrunch.com/feed/"
    },
    {
        "name": "The Verge",
        "url": "https://www.theverge.com/rss/index.xml"
    }
]

# Keyword mappings for categorization
CATEGORY_KEYWORDS = {
    "AI": ["ai", "artificial intelligence", "machine learning", "deep learning", "openai", "chatgpt", "neural network"],
    "Semiconductors": ["semiconductor", "chip", "nvidia", "intel", "amd", "tsmc", "microchip"],
    "Robotics": ["robot", "robotics", "automation", "boston dynamics"],
    "Electronics": ["electronics", "smartphone", "apple", "samsung", "gadget", "wearable"],
    "EV": ["ev", "electric vehicle", "tesla", "rivian", "battery"],
    "Space": ["space", "nasa", "spacex", "satellite", "orbit", "mars"],
    "Other": [] # Default category if none match
}

CATEGORIES = list(CATEGORY_KEYWORDS.keys())
