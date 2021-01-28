import json
from django.views.generic import View

from interface_app import common
from interface_app.form.debug import DebugForm
from interface_app.utils.interface_utils import InterfaceUtils


class TestList0Views(View):
    def post(self, request, *args, **kwargs):
        """
        测试的post请求
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        print(request.body)
        params = json.loads(body)
        test = params.get('test', None)
        if test is not None:
            return common.response_success(params)
        else:
            return common.response_failed()

    def put(self, request, *args, **kwargs):
        """
        测试的put请求
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        test = params.get('test', None)
        if test is not None:
            return common.response_success(params)
        else:
            return common.response_failed()

    def delete(self, request, *args, **kwargs):
        """
        测试的delete请求
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        params = json.loads(body)
        test = params.get('test', None)
        if test is not None:
            return common.response_success(params)
        else:
            return common.response_failed()
