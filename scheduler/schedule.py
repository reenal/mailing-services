from apscheduler.schedulers.blocking import BlockingScheduler
from scheduler.job import job_function


schedule = BlockingScheduler()
schedule.add_job(job_function, 'cron', minute=0)

schedule.start()
