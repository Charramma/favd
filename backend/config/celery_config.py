from celery.schedules import crontab

# 配置Broker
BROKER_URL = "redis://192.168.5.87:6379/1"
# 配置结果存储
CELERY_RESULT_BACKEND = "redis://192.168.5.87:6379/2"
# 导入一些任务
CELERY_IMPORTS = {
    'celery_app.tasks',
}
# 定义一些定时任务（非必须）
CELERY_SCHEDULE = {
    # every-minute为自定义的任务名
    'every-minute': {
        # task 要执行的任务，这里指定执行celery_app/tasks.py中的scheduled_task任务
        'task': 'celery_app.tasks.scheduled_task',
        'schedule': crontab(minute='*/1'),
        # 'args': (1, 2),
        # 'schedule': timedelta(seconds=5)
    }
}
