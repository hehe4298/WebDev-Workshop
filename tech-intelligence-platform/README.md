# Tech Intelligence Platform

Version 1 of the Tech Intelligence Platform - A modular, maintainable, and production-style technology news intelligence system.

## Features (Version 1)
- **RSS Collection:** Automatically collects technology news from configured RSS feeds (Reuters, TechCrunch, The Verge).
- **Article Scraping:** Visits article URLs to extract readable article content.
- **Database Storage:** Stores articles in an SQLite database using SQLAlchemy ORM, preventing duplicates.
- **Categorization:** Keyword-based categorization of articles (AI, Semiconductors, Robotics, Electronics, EV, Space, Other).
- **Report Generation:** Generates professional DOCX reports summarizing the collected articles by category.
- **Scheduler:** Runs collection automatically every 2 hours and report generation at 08:00 AM and 08:00 PM using APScheduler.
- **Logging:** Centralized logging of collections, reports, and errors to `logs/app.log`.

## Installation

1. Clone the repository.
2. Ensure you have Python 3.11+ installed.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Architecture & Folder Structure

The project is designed with a modular architecture to allow future modules (Importance scoring, Deduplication, Historical memory, LLM summarization, Image collection, Trend detection, Breaking alerts, Dashboard) to be added without major rewrites.

- `src/config/`: Configuration settings and keyword mappings.
- `src/database/`: Database connection and session management setup.
- `src/models/`: SQLAlchemy ORM models for Articles and Reports.
- `src/collectors/`: RSS feed reading, content extraction, and article collection logic.
- `src/categorization/`: Logic to assign categories based on keywords.
- `src/reporting/`: Logic for generating DOCX reports.
- `src/scheduler/`: APScheduler setup and task definitions.
- `src/utils/`: Utility functions like custom logging.
- `tests/`: Pytest suite covering all major components.
- `reports/`: Generated DOCX reports are saved here.
- `logs/`: Application logs are saved here.
- `main.py`: Entry point for running the platform (scheduler and manual execution).

## How to run manually

To start the scheduler and run the application continuously:
```bash
cd tech-intelligence-platform
python main.py
```
*Note: `main.py` may also include command-line arguments to run specific tasks immediately (e.g., `--collect` or `--report`). Check `main.py` for more details.*

## How to run tests

To run the complete test suite and generate coverage reports:
```bash
cd tech-intelligence-platform
pytest --cov=src tests/
```

## Future Roadmap
Future iterations of this platform will introduce the following modules:
- Importance scoring
- Deduplication
- Historical memory
- LLM summarization
- Image collection
- Trend detection
- Breaking alerts
- Dashboard
