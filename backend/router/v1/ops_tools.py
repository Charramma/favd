from libs.nestable_blueprint import NestableBlueprint
from flask_restful import Api, Resource
from libs.handler import default_error_handler
from models.ops_tools import Task, TaskLog
from flask import request, current_app, g
from sqlalchemy import or_
from celery_app.tasks import remote_ssh
from models.user import UserProfile
from models.extension import db
from libs.response import generate_response
from serializer.ops_tools import tasks_schema, task_schema, tasklog_schema, tasklogs_schema
from libs.authorize import auth, permission_required

ops_tools_bp = NestableBlueprint('ops_tools_v1', __name__, url_prefix='ops_tools/')
# 定义restapi对象
api = Api(ops_tools_bp)

# 指定当出现异常时，所调用的处理方法
# 当需要看到真实的错误信息时，请把下面这一句注释掉
api.handle_error = default_error_handler


class TasksView(Resource):
    @auth.login_required
    def get(self):
        # 获取参数 => 参数默认获取到的都是str类型
        params = request.args
        keywords = params.get("keywords", "")
        page = int(params.get("page", 1))
        per_page = int(params.get("pagesize", current_app.config["PER_PAGE"]))

        # 根据参数查询结果
        if keywords:
            result = Task.query.filter(or_(Task.task_name.contains(keywords), Task.task_command.contains(keywords),
                                           Task.task_host.contains(keywords)))
        else:
            result = Task.query

        # 分页
        paginate_tasks = result.paginate(page, per_page=per_page, error_out=False)

        # 生成要返回的数据
        tasks = paginate_tasks.items

        return generate_response(data=tasks_schema.dump(tasks), count=paginate_tasks.total)

    @auth.login_required
    def post(self):
        # 获取参数
        params = request.json
        task_name = params.get("task_name", "")
        task_command = params.get("task_command", "")
        task_args = params.get("task_args", "")
        task_host = params.get("task_host", "")
        # 验证参数合法性wtforms

        # 新建Task
        task = Task(task_name=task_name, task_command=task_command,
                    task_args=task_args, task_host=task_host)
        db.session.add(task)
        db.session.commit()

        # 数据序列化并返回
        return generate_response(data=task_schema.dump(task))


class TaskView(Resource):
    @auth.login_required
    def put(self, task_id):
        # 获取参数
        params = request.json
        task_name = params.get("task_name", "")
        task_command = params.get("task_command", "")
        task_args = params.get("task_args", "")
        task_host = params.get("task_host", "")
        # 验证参数合法性wtforms

        # 编辑Task
        task = Task.query.get(task_id)
        task.task_name = task_name
        task.task_command = task_command
        task.task_host = task_host
        task.task_args = task_args
        db.session.add(task)
        db.session.commit()

        # 数据序列化并返回
        return generate_response(data=task_schema.dump(task))


class RunTaskView(Resource):
    @auth.login_required
    def get(self, task_id):
        # 执行任务 => 代码健壮性(try.except, if...else)
        task = Task.query.get(task_id)
        ret = remote_ssh.delay(task.task_host, task.task_command)
        # user = UserProfile.query.get(g.user["uid"])
        # 写日志
        tasklog = TaskLog(task_id=task_id, tasklog_tid=ret.task_id, user=g.user["uid"])
        db.session.add(tasklog)
        db.session.commit()
        # 返回结果
        return generate_response(data=tasklog_schema.dump(tasklog))


# 获取所有日志，如果result为空，则取值并修改。

from celery.result import AsyncResult
from celery_app import celery


class TaskLogsView(Resource):

    @auth.login_required
    @permission_required
    def get(self):
        # 可以分页、查询。。。。
        tasklogs = TaskLog.query.all()

        for tasklog in tasklogs:
            res = AsyncResult(tasklog.tasklog_tid, app=celery)
            # 任务的返回值 => remote_ssh函数的返回值
            tasklog.tasklog_result = res.result
            # 任务的状态 =>
            tasklog.tasklog_status = res.status
            db.session.add(tasklog)
        db.session.commit()
        return generate_response(data=tasklogs_schema.dump(tasklogs), total=len(tasklogs))


api.add_resource(TasksView, '/tasks/')
api.add_resource(TaskView, '/tasks/<task_id>/')
api.add_resource(RunTaskView, '/run/<task_id>/')
api.add_resource(TaskLogsView, '/tasklogs/')
