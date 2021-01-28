import json
from interface_app import common
from interface_app.form.service import ServiceForm
from interface_app.models.service import Service, IS_ROOT
from interface_app.utils.service_utils import ServiceUtils

from django.views.generic import View
from interface_app.my_exception import MyException


class ServiceListViews(View):
    def get(self, request, *args, **kwargs):
        """
        获取服务列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = ServiceUtils.get_service_tree_recursion(IS_ROOT)
        return common.response_success(ret)

    def post(self, request, *args, **kwargs):
        """
        创建服务
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        form = ServiceForm(params)
        result = form.is_valid()
        if result:
            service = Service.objects.create(**form.changed_data)
            if service:
                return common.response_success()
            else:
                raise MyException('创建失败')
        else:
            return common.response_failed()