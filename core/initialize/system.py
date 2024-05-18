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