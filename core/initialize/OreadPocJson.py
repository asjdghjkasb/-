import json
import os

class RequestResponseData:
    def __init__(self, json_data):
        self.request = json_data.get('request', {})
        self.response = json_data.get('response', {})

    @classmethod
    def from_json_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        return cls(json_data)

    def __repr__(self):
        return f"RequestResponseData(request={self.request}, response={self.response})"

# 使用示例
if __name__ == "__main__":
    # 假设你有一个目录，里面存放了多个 JSON 文件
    json_directory = 'path/to/json/files'

    # 读取所有 JSON 文件并创建对象
    json_files = [f for f in os.listdir(json_directory) if f.endswith('.json')]
    data_objects = [RequestResponseData.from_json_file(os.path.join(json_directory, json_file)) for json_file in json_files]

    # 打印每个对象的数据
    for data in data_objects:
        print(data)
