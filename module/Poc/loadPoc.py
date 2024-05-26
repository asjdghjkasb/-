import json
import os


class PocLoader:
    """
    POC加载器类，用于从指定目录加载POC（Proof of Concept）文件。

    :param directory_path: POC文件所在的目录路径
    """

    def __init__(self, directory_path):
        self.directory_path = directory_path

    def load_pocs(self, finger):
        """
        根据指定的特征加载POC文件。

        :param finger: 特征标识，用于选择特定的POC文件。当前仅支持"pikachu"。
        :return: 返回一个包含加载成功POC数据的列表。如果指定的特征不为"pikachu"或没有找到POC文件，则返回空列表。
        """
        if finger == "pikachu":
            # 在目录中查找所有.json文件
            poc_files = [f for f in os.listdir(self.directory_path) if
                         os.path.isfile(os.path.join(self.directory_path, f)) and f.endswith('.json')]

            if not poc_files:
                print("No POC files found in the directory.")
                return []

            print("Available POC files:")
            for idx, poc_file in enumerate(poc_files):
                print(f"{idx + 1}: {poc_file}")

            # 提示用户选择要加载的POC文件，可以输入编号选择单个或默认加载所有
            file_selection = input("请选择需要检测的poc(输入编号，默认使用所有poc):").strip()

            if file_selection.isdigit() and 1 <= int(file_selection) <= len(poc_files):
                # 如果用户输入了有效的文件编号，则仅加载指定的POC文件
                selected_files = [poc_files[int(file_selection) - 1]]
            else:
                # 否则，加载所有找到的POC文件
                selected_files = poc_files

            # 加载选中的POC文件内容
            loaded_pocs = []
            for filename in selected_files:
                file_path = os.path.join(self.directory_path, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        loaded_pocs.append(data)
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON file {filename}: {e}")
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

            return loaded_pocs

        return []
