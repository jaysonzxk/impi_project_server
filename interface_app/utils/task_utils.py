from django.forms.models import model_to_dict
from interface_app.models.result import TaskResult, InterfaceResult


class TaskUtils:

    @classmethod
    def get_result_summary(cls, result_id):
        ret = {
            'success': 0,
            'failed': 0,
            'total': 0
        }
        if not result_id:
            return ret

        v = InterfaceResult.objects.filter(task_result_id=result_id)
        for i in v:
            if i.success:
                ret['success'] += 1
            else:
                ret['failed'] += 1
        ret['total'] = ret['success'] + ret['failed']
        return ret

    @classmethod
    def get_last_result_summary(cls, task_id):
        if not task_id:
            return cls.get_result_summary(None)
        result = cls.get_last_result(task_id)
        if not result:
            return cls.get_result_summary(None)
        else:
            ret = cls.get_result_summary(result.id)
            return ret

    @classmethod
    def get_last_result(cls, task_id):
        if not task_id:
            return None
        result = TaskResult.objects.filter(task_id=task_id).order_by('-id')
        if len(result) == 0:
            return None
        else:
            return result[0]

    @classmethod
    def get_last_interface_result(cls, result_id, interface_id):
        if not result_id or interface_id:
            return '无'
        v = InterfaceResult.objects.filter(task_result_id=result_id, interface_id=interface_id)
        if len(v) == 0:
            return '无'

        if v[0].success:
            return '成功'
        else:
            return '失败'
