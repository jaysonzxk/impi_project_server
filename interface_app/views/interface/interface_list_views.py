import json
from django.forms.models import model_to_dict
from django.views.generic import View

from interface_app import common
from interface_app.form.interface import InterfaceForm
from interface_app.models.interface import Interface
from interface_app.my_exception import MyException


class InterfaceListViews(View):
    def get(self, request, *args, **kwargs):
        """
        获取全部接口列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        interfaces = Interface.objects.all()
        ret = []
        for i in interfaces:
            ret.append(model_to_dict(i))
        return common.response_success(ret)

    def post(self, request, *args, **kwargs):
        """
        创建接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        form = InterfaceForm(params)
        result = form.is_valid()
        if result:
            interface = Interface.objects.create(**form.changed_data)
            if interface:
                return common.response_success()
            else:
                raise MyException('创建失败')
        else:
            return common.response_failed()