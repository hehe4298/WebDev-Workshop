import os
from datetime import datetime
from src.reporting.generator import generate_report
from src.models.models import Article

def test_generate_report_empty(test_session):
    filepath = generate_report()
    assert filepath != ""
    assert os.path.exists(filepath)
    os.remove(filepath)

def test_generate_report_with_data(test_session):
    article = Article(
        title="AI Breakthrough",
        source="Test Source",
        url="http://test.com/ai",
        published_date=datetime.now(),
        content="This is a test article about AI. " * 50, # make it long enough
        category="AI"
    )
    test_session.add(article)
    test_session.commit()

    filepath = generate_report()
    assert filepath != ""
    assert os.path.exists(filepath)
    os.remove(filepath)
