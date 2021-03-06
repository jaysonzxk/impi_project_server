from django.db import models
from interface_app.models.base import Base
from interface_app.models.interface import Interface


TASK_STATUS = (
    (0, '未执行'),
    (1, '正在执行'),
    (2, '执行完成'),
)


class Task(models.Model, Base):
    """
    任务的表结构
    """
    name = models.CharField('name', blank=False, default='', max_length=200)
    description = models.TextField('description', blank=True, default='')
    status = models.IntegerField('状态', choices=TASK_STATUS, default=0)

    def __str__(self):
        return self.name


class TaskInterface(models.Model, Base):
    """
    任务和接口的关系表
    """
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    interface = models.ForeignKey(Interface, on_delete=models.SET_NULL, null=True)