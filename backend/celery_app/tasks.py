import time
import random
from . import celery
import paramiko


# 注册一个任务
@celery.task
def scheduled_task():
    print(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())))
    print("this is a scheduled_task!! 1 min")


@celery.task
def celery_task(sth):
    print(f"{sth} celery_task start~~~")
    time.sleep(random.randint(2, 5))
    print(f"{sth} celery_task end~~~")
    return sth


# 任务 => host, cmd
@celery.task
def remote_ssh(host, cmd):
    try:
        # 创建ssh客户端
        ssh = paramiko.SSHClient()
        # 自动添加
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接主机
        ssh.connect(host, 22, timeout=5)
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        stdin = stdin.read()
        err = stderr.read()
        out = stdout.read()
        result = out if out else err
        result = result.decode("utf-8")
        print(err, out, stdin)
        if not result:
            result = "执行成功"
        # 断开连接连接
        ssh.close()
    except Exception as ex:
        print(ex)
        result = "执行出错！！"
    return result
