from apscheduler.schedulers.blocking import BlockingScheduler
from scheduler.job import job_function
from scheduler.job import job_function1

schedule = BlockingScheduler()

# working cron which run every minute for mon-fri
# schedule.add_job(job_function, 'cron',day_of_week='mon-fri',hour='*',minute='*')

#this will work everyday at a 10.15 am
schedule.add_job(job_function1, 'cron', day_of_week='*', hour='10', minute='15')

schedule.start()
