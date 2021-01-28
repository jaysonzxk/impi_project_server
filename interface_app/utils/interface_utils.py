import requests
import traceback


class InterfaceUtils:

    @classmethod
    def parse_parameter(cls, parameter):
        """
        form形式的参数转成字典，例如 [{'key': 'a', 'value': 'a', 'type': 'string'}, {'key': 'b', 'value': '1', 'type': 'int'}]
        会转成字典：{"a": "a", "b": 1}
        :param parameter:
        :return:
        """
        ret = {}
        if not parameter:
            return ret

        for p in parameter:
            try:
                p_type = p.get('type', None)
                if p_type is None:
                    continue
                key = p.get('key', None)
                if key is None:
                    continue
                value = p.get('value', None)
                if value is None:
                    continue
                if p_type == 'string':
                    ret[key] = str(value)
                elif p_type == 'int':
                    ret[key] = int(value)
                elif p_type == 'float':
                    ret[key] = float(value)
                elif p_type == 'bool':
                    ret[key] = bool(value)
                else:
                    continue
            except Exception:
                continue
        return ret

    @classmethod
    def send_request(cls, url, method, header, parameter, parameter_type):
        ret = ''
        if parameter_type == 'form':
            parameter = cls.parse_parameter(parameter)

        try:
            if method == 'GET':
                ret = cls.__get_request(url, header, parameter)
            elif method == 'POST':
                ret = cls.__post_request(url, header, parameter, parameter_type)
            elif method == 'PUT':
                ret = cls.__put_request(url, header, parameter, parameter_type)
            elif method == 'DELETE':
                ret = cls.__delete_request(url, header, parameter, parameter_type)
            return ret
        except Exception:
            return traceback.format_exc()

    @classmethod
    def __set_header(cls, header, parameter_type):
        if parameter_type == 'json':
            header['content-type'] = 'application/json'
        else:
            header['content-type'] = 'application/x-www-form-urlencoded'
        return header

    @classmethod
    def __get_request(cls, url, header, parameter):
        """
        get请求，数据都在url，超时30s
        :param url:字符串
        :param header:字典
        :param parameter:字典
        :return:
        """
        ret = requests.get(url, params=parameter, headers=header, timeout=30)
        return ret

    @classmethod
    def __post_request(cls, url, header, parameter, parameter_type):
        """
        post 请求
        :param url:
        :param header:
        :param parameter:
        :param parameter_type:
        :return:
        """
        header = cls.__set_header(header, parameter_type)
        if parameter_type == 'json':
            ret = requests.post(url, json=parameter, headers=header, timeout=30)
        else:
            ret = requests.post(url, data=parameter, headers=header, timeout=30)
        return ret.text

    @classmethod
    def __delete_request(cls,url, header, parameter,parameter_type):
        """
        delete请求
        :param url:
        :param header:
        :param parameter:
        :param parameter_type:
        :return:
        """
        header = cls.__set_header(header, parameter_type)
        if parameter_type == 'json':
            ret = requests.delete(url, json=parameter, headers=header, timeout=30)
        else:
            ret = requests.delete(url, data=parameter, headers=header, timeout=30)
        return ret.text

    @classmethod
    def __put_request(cls, url, header, parameter, parameter_type):
        """
        put请求
        :param url:
        :param header:
        :param parameter:
        :param parameter_type:
        :return:
        """
        header = cls.__set_header(header, parameter_type)
        if parameter_type == 'json':
            ret = requests.put(url, json=parameter, headers=header, timeout=30)
        else:
            ret = requests.put(url, data=parameter, headers=header, timeout=30)
        return ret.text