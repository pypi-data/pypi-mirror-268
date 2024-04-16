from apscheduler.schedulers.background import BackgroundScheduler

def load_jieba_dict(manager):
    manager.load_jieba_dict()

def scheduler(manager, hour = 1):
    scheduler = BackgroundScheduler()
    scheduler.add_job(load_jieba_dict, 'cron', args=[manager], hour=hour)
    scheduler.start()
