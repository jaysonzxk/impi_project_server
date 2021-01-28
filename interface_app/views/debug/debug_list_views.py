import json
from django.views.generic import View

from interface_app import common
from interface_app.form.debug import DebugForm
from interface_app.utils.interface_utils import InterfaceUtils


class DebugListViews(View):
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
        form = DebugForm(params)
        result = form.is_valid()
        if result:
            url = form.changed_data['url']
            method = form.changed_data['method']
            header = form.changed_data['header']
            parameter = form.changed_data['parameter']
            parameter_type = form.changed_data['parameter_type']
            ret = InterfaceUtils.send_request(url, method, header, parameter, parameter_type)
            return common.response_success(ret)
        else:
            return common.response_failed()