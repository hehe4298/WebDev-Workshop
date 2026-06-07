from apscheduler.schedulers.background import BackgroundScheduler
import time

from src.utils.logger import logger
from src.collectors.rss_collector import collect_articles
from src.reporting.generator import generate_report

def start_scheduler():
    """
    Initializes and starts the APScheduler with configured tasks.
    """
    scheduler = BackgroundScheduler()

    # Collection: Every 2 hours
    scheduler.add_job(
        func=collect_articles,
        trigger="interval",
        hours=2,
        id="collect_articles_job",
        name="Collect articles from RSS feeds every 2 hours",
        replace_existing=True
    )

    # Report Generation: 08:00 AM
    scheduler.add_job(
        func=generate_report,
        trigger="cron",
        hour=8,
        minute=0,
        id="generate_report_am",
        name="Generate morning report",
        replace_existing=True
    )

    # Report Generation: 08:00 PM (20:00)
    scheduler.add_job(
        func=generate_report,
        trigger="cron",
        hour=20,
        minute=0,
        id="generate_report_pm",
        name="Generate evening report",
        replace_existing=True
    )

    scheduler.start()
    logger.info("Scheduler started successfully")
    return scheduler
