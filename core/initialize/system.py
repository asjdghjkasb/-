import os
import platform

def os_check():
    if platform.system().lower() == 'windows':
        return "windows"
    elif platform.system().lower() == 'linux':
        return "linux"
    else:
        return "other"

def path_check(current_os):
    if current_os == "windows":
        # 获取 Windows 中脚本运行的路径
        script_path = os.path.abspath(os.path.dirname(__file__))
        return script_path
    elif current_os == "linux":
        # 获取 Linux 中脚本运行的路径
        script_path = os.path.abspath(os.path.dirname(__file__))
        return script_path
    else:
        return "脚本路径获取失败"

