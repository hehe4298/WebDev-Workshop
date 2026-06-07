from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    source = Column(String, nullable=False)
    url = Column(String, nullable=False, unique=True)
    published_date = Column(DateTime, nullable=True)
    content = Column(Text, nullable=True)
    category = Column(String, nullable=True)
    collected_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Article(title='{self.title}', source='{self.source}', url='{self.url}')>"

class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True, autoincrement=True)
    report_name = Column(String, nullable=False)
    generated_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Report(report_name='{self.report_name}', generated_at='{self.generated_at}')>"
