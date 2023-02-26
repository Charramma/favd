from celery import Celery

celery = Celery("celery_app")

# 导入配置文件
celery.config_from_object('config.celery_config')
