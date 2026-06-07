from src.scheduler.tasks import start_scheduler
import time

def test_scheduler_configuration():
    scheduler = start_scheduler()
    jobs = scheduler.get_jobs()

    # Verify jobs are added
    assert len(jobs) == 3
    job_ids = [job.id for job in jobs]
    assert "collect_articles_job" in job_ids
    assert "generate_report_am" in job_ids
    assert "generate_report_pm" in job_ids

    scheduler.shutdown()
