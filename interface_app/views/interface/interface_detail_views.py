import json
from django.forms.models import model_to_dict
from django.views.generic import View

from interface_app import common
from interface_app.form.interface import InterfaceForm
from interface_app.models.interface import Interface
from interface_app.my_exception import MyException


class InterfaceDetailViews(View):
    def get(self, request, pk, *args, **kwargs):
        """
        获取单个接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            interface = Interface.objects.get(id=pk)
        except Interface.DoesNotExist:
            return common.response_failed()
        else:
            return common.response_success(model_to_dict(interface))

    def put(self, request, pk, *args, **kwargs):
        """
        更新单个接口
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        form = InterfaceForm(params)
        result = form.is_valid()
        if result:
            Interface.objects.filter(id=pk).update(**form.changed_data)
        else:
            raise MyException()
        return common.response_success()

    def delete(self, request, pk, *args, **kwargs):
        """
        删除单个接口
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        Interface.objects.filter(id=pk).delete()
        return common.response_success()