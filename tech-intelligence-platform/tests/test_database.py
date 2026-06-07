from datetime import datetime
from src.models.models import Article, Report

def test_create_article(test_session):
    article = Article(
        title="Test Article",
        source="Test Source",
        url="http://test.com/1",
        published_date=datetime.now(),
        content="Test content",
        category="AI"
    )
    test_session.add(article)
    test_session.commit()

    fetched = test_session.query(Article).first()
    assert fetched is not None
    assert fetched.title == "Test Article"
    assert fetched.url == "http://test.com/1"

def test_duplicate_article_url(test_session):
    article1 = Article(
        title="Test Article 1",
        source="Test Source",
        url="http://test.com/duplicate"
    )
    test_session.add(article1)
    test_session.commit()

    article2 = Article(
        title="Test Article 2",
        source="Test Source",
        url="http://test.com/duplicate"
    )
    test_session.add(article2)

    from sqlalchemy.exc import IntegrityError
    import pytest
    with pytest.raises(IntegrityError):
        test_session.commit()

def test_create_report(test_session):
    report = Report(report_name="test_report.docx")
    test_session.add(report)
    test_session.commit()

    fetched = test_session.query(Report).first()
    assert fetched is not None
    assert fetched.report_name == "test_report.docx"
