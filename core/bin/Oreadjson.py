import json

class RequestResponse:
    def __init__(self, data):
        # 初始化RequestResponse类
        self.request = data.get('request', {})
        self.response = data.get('response', {})

    def __repr__(self):
        # 返回RequestResponse对象的字符串表示
        return f"RequestResponse(request={self.request}, response={self.response})"

class PocData:
    def __init__(self, json_data):
        # 初始化PocData类
        self.name = json_data.get('name', '')
        self.comment = json_data.get('comment', '')
        self.version = json_data.get('version', '')
        self.main_request = {key: RequestResponse(value) for key, value in json_data.get('mainRequest', {}).items()}

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
        return f"PocData(name={self.name}, comment={self.comment}, version={self.version}, main_request={self.main_request})"

    def display(self):
        # 打印PocData对象的内容
        print(f"Name: {self.name}")
        print(f"Comment: {self.comment}")
        print(f"Version: {self.version}")
        print("Main Requests:")
        for key, req_res in self.main_request.items():
            print(f"  Request {key}:")
            print(f"    Request: {req_res.request}")
            print(f"    Response: {req_res.response}")

