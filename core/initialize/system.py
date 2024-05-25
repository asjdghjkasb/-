import os
import platform

def os_check():
    if platform.system().lower() == 'windows':
        return "windows"
    elif platform.system().lower() == 'linux':
        return "linux"
    else:
        return "other"

def path_add(base_path, *paths):  # 路径增加处理
    if not base_path:
        raise ValueError("基础路径不能为空")

    if not all(isinstance(p, str) and p for p in paths):
        raise ValueError("所有附加路径必须是非空字符串")

    try:
        for add_path in paths:
            base_path = os.path.join(base_path, add_path)
        return base_path
    except Exception as e:
        raise RuntimeError(f"连接路径时发生错误: {e}")

def path_check(path,filename=None):
    if not isinstance(path, str):
        raise ValueError("路径必须是字符串")
    
    if not path:
        raise ValueError("路径不能为空")

    try:
        if os.path.exists(path):
            return True
        else:
            return False
    except Exception as e:
        raise RuntimeError(f"检查路径时发生错误: {e}")
    
def findAllFilePathName(path):
    # 检查路径是否存在
    if not path_check(path):
        raise ValueError("路径不存在")
    
    # 检查路径是否为文件夹
    if not os.path.isdir(path):
        raise ValueError("路径必须是文件夹")
    
    # 获取所有子文件夹的名称
    folder_list = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    return folder_list

# 获目录下的全部文件名称
def get_all_files_name(path):
    # 检查路径是否存在
    if not path_check(path):
        raise ValueError("路径不存在")
    
    # 检查路径是否为文件夹
    if not os.path.isdir(path):
        raise ValueError("路径必须是文件夹")
    
    # 获取所有子文件夹的名称
    return [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]

# 获取目录下的全部文件路径
def getAllFilePath(path):
    # 检查路径是否存在
    if not path_check(path):
        raise ValueError("路径不存在")
    
    # 检查路径是否为文件夹
    if not os.path.isdir(path):
        raise ValueError("路径必须是文件夹")
    
    # 获取所有子文件夹的路径
    return [os.path.join(root, file) for root, dirs, files in os.walk(path) for file in files]


################   test方法   ################### 
