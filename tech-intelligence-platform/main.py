import argparse
import time
import sys

from src.database.db import init_db
from src.utils.logger import logger
from src.collectors.rss_collector import collect_articles
from src.reporting.generator import generate_report
from src.scheduler.tasks import start_scheduler

def main():
    parser = argparse.ArgumentParser(description="Tech Intelligence Platform")
    parser.add_argument("--collect", action="store_true", help="Run RSS collection immediately")
    parser.add_argument("--report", action="store_true", help="Generate report immediately")
    parser.add_argument("--schedule", action="store_true", help="Start the scheduler and run continuously")

    args = parser.parse_args()

    # Initialize database
    logger.info("Initializing database...")
    init_db()

    if args.collect:
        logger.info("Starting manual collection...")
        collect_articles()

    if args.report:
        logger.info("Starting manual report generation...")
        generate_report()

    if args.schedule:
        logger.info("Starting scheduler...")
        scheduler = start_scheduler()

        try:
            # Keep the main thread alive
            while True:
                time.sleep(2)
        except (KeyboardInterrupt, SystemExit):
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler stopped.")

    if not (args.collect or args.report or args.schedule):
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
