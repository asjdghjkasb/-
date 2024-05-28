import json

class RequestResponse:
    def __init__(self, data):
        # 初始化RequestResponse类
        request_data = data.get('request', {})
        response_data = data.get('response', {})
        
        self._request_host = request_data.get('host', '')
        self._request_method = request_data.get('method', '')
        self._request_path = request_data.get('path', '')
        self._request_cookie = request_data.get('cookie', '')
        self._request_header = request_data.get('requestheader', '')
        self._request_body = request_data.get('requestbody', '')

        self._response_status_code = response_data.get('statuscode', '')
        self._response_status_message = response_data.get('statusmessage', '')
        self._response_time = response_data.get('responsetime', '')
        self._response_header = response_data.get('responseheader', '')
        self._response_body = response_data.get('responsebody', '')

    @property
    def request_host(self):
        return self._request_host

    @request_host.setter
    def request_host(self, value):
        self._request_host = value

    @property
    def request_method(self):
        return self._request_method

    @request_method.setter
    def request_method(self, value):
        self._request_method = value

    @property
    def request_path(self):
        return self._request_path

    @request_path.setter
    def request_path(self, value):
        self._request_path = value

    @property
    def request_cookie(self):
        return self._request_cookie

    @request_cookie.setter
    def request_cookie(self, value):
        self._request_cookie = value

    @property
    def request_header(self):
        return self._request_header

    @request_header.setter
    def request_header(self, value):
        self._request_header = value

    @property
    def request_body(self):
        return self._request_body

    @request_body.setter
    def request_body(self, value):
        self._request_body = value

    @property
    def response_status_code(self):
        return self._response_status_code

    @response_status_code.setter
    def response_status_code(self, value):
        self._response_status_code = value

    @property
    def response_status_message(self):
        return self._response_status_message

    @response_status_message.setter
    def response_status_message(self, value):
        self._response_status_message = value

    @property
    def response_time(self):
        return self._response_time

    @response_time.setter
    def response_time(self, value):
        self._response_time = value

    @property
    def response_header(self):
        return self._response_header

    @response_header.setter
    def response_header(self, value):
        self._response_header = value

    @property
    def response_body(self):
        return self._response_body

    @response_body.setter
    def response_body(self, value):
        self._response_body = value

    def __repr__(self):
        # 返回RequestResponse对象的字符串表示
        return (f"RequestResponse(request={{'host': '{self.request_host}', 'method': '{self.request_method}', "
                f"'path': '{self.request_path}', 'cookie': '{self.request_cookie}', "
                f"'requestheader': '{self.request_header}', 'requestbody': '{self.request_body}'}}, "
                f"response={{'statuscode': '{self.response_status_code}', 'statusmessage': '{self.response_status_message}', "
                f"'responsetime': '{self.response_time}', 'responseheader': '{self.response_header}', "
                f"'responsebody': '{self.response_body}'}})")


class PocData:
    def __init__(self, json_data):
        # 初始化PocData类
        self._name = json_data.get('name', '')
        self._vuln = json_data.get('vuln', '')
        self._version = json_data.get('version', '')
        self._comment = json_data.get('comment', '')
        self._type = json_data.get('type', '')
        self._main_request = {key: RequestResponse(value) for key, value in json_data.get('mainRequest', {}).items()}


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def vuln(self):
        return self._vuln

    @vuln.setter
    def vuln(self, value):
        self._vuln = value

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def main_request(self):
        return self._main_request

    @main_request.setter
    def main_request(self, value):
        self._main_request = {key: RequestResponse(val) for key, val in value.items()}

    def get_main_request_by_key(self, key):
        return self._main_request.get(key)
    
    def get_main_request_key_count(self):
        """
        返回mainRequest中键的个数
        :return: mainRequest字典中键的个数
        """
        return len(self._main_request)

    @classmethod
    def from_json_file(cls, file_path):
        """
        从JSON文件加载数据并返回PocData对象
        :param file_path: JSON文件的路径
        :return: PocData对象
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
            return cls(json_data)
        except FileNotFoundError:
            print(f"文件未找到: {file_path}")
        except json.JSONDecodeError:
            print(f"文件解码错误: {file_path}")
        except Exception as e:
            print(f"加载文件时发生错误: {e}")

    def __repr__(self):
        # 返回PocData对象的字符串表示
        return f"PocData(name={self.name}, vuln={self.vuln}, comment={self.comment}, version={self.version}, main_request={self.main_request})"

    def display(self):
        # 打印PocData对象的内容
        print(f"Name: {self.name}")
        print(f"Vuln: {self.vuln}")
        print(f"Comment: {self.comment}")
        print(f"Version: {self.version}")
        print("Main Requests:")
        for key, req_res in self.main_request.items():
            print(f"  Request {key}:")
            print(f"    Request: {req_res.request}")
            print(f"    Response: {req_res.response}")

# 示例使用
if __name__ == "__main__":
    file_path = "path_to_your_json_file.json"
    poc_data = PocData.from_json_file(file_path)
    if poc_data:
        poc_data.display()
