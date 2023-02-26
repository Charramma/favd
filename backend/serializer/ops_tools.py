from models.ops_tools import Task, TaskLog
from .extension import ma


class TaskSchema(ma.Schema):
    class Meta:
        model = Task
        fields = ('task_id', 'task_name', 'task_command', 'task_host')


class TaskLogSchema(ma.Schema):
    class Meta:
        model = TaskLog
        fields = ('tasklog_id', 'tasklog_result', 'tasklog_staus', 'tasklog_tid', 'tasklog_status')


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
tasklog_schema = TaskLogSchema()
tasklogs_schema = TaskLogSchema(many=True)