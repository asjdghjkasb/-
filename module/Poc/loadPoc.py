import json
import os
import module.Poc.execUPoc as exePoc

def load_poc(finger):
    if finger == "pikachu":
        directory_path = r'C:\Users\87788\Desktop\Vulnerability-scanning\module\Poc\pikachuPoc'
        for filename in os.listdir(directory_path):  
            # 构建文件的完整路径  
            file_path = os.path.join(directory_path, filename)  
            
            # 检查文件是否是一个文件（而不是目录）  
            if os.path.isfile(file_path):  
                # 检查文件扩展名是否为.json  
                if filename.endswith('.json'):  
                    try:  
                        # 打开并读取JSON文件  
                        with open(file_path, 'r', encoding='utf-8') as f:  
                            data = json.load(f)  # 解析JSON数据  
                            # print(data)
                            result = exePoc.exe_poc(data)
                            if result != "":
                                return result
                    except json.JSONDecodeError as e:  
                        print(f"Error parsing JSON file {filename}: {e}")  
                    except Exception as e:  
                        print(f"Error reading file {filename}: {e}")  

# if __name__ == '__main__':
#     load_poc('pikachu')