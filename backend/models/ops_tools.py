import datetime
from .extension import db


class Task(db.Model):
    """用于存储具体任务信息"""
    __tablename__ = "task"
    task_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    task_name = db.Column(db.String(64), nullable=False, comment="任务名")
    task_command = db.Column(db.String(256), nullable=False, comment="任务要执行的命令")
    task_args = db.Column(db.String(256), comment="命令的参数")
    task_host = db.Column(db.String(16), nullable=False, comment="待执行命令的主机")

    tasklogs = db.relationship("TaskLog", backref="task")


class TaskLog(db.Model):
    """用于存储日志执行结果"""
    __tablename__ = "tasklog"
    tasklog_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    task_id = db.Column(db.ForeignKey('task.task_id'), nullable=False, comment="关联的任务id")
    tasklog_tid = db.Column(db.String(64), nullable=False, comment="celery任务的id")
    tasklog_result = db.Column(db.Text, comment="任务执行结果")
    tasklog_status = db.Column(db.String(24), comment="任务执行状态")
    tasklog_create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment="任务创建时间")
    user = db.Column(db.ForeignKey("user_profile.user_profile_id"), comment="触发任务的用户")
