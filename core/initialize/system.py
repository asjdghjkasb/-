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

def path_check(path):
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

def test_path_check():
    # 测试存在的路径
    existing_path = os.path.abspath(os.path.dirname(__file__))  # 当前脚本的路径
    assert path_check(existing_path) == True, "Test failed for an existing path"
    print(f"path_check(existing_path) passed: {existing_path}")
    
    # 测试不存在的路径
    non_existing_path = os.path.join(existing_path, "non_existing_folder")
    assert path_check(non_existing_path) == False, "Test failed for a non-existing path"
    print(f"path_check(non_existing_path) passed: {non_existing_path}")
    
    # 测试空路径
    try:
        path_check("")
    except ValueError as ve:
        print(f"ValueError as expected for empty path: {ve}")
    
    # 测试非字符串路径
    try:
        path_check(123)
    except ValueError as ve:
        print(f"ValueError as expected for non-string path: {ve}")
    
    # 测试错误处理
    try:
        invalid_path = None
        path_check(invalid_path)
    except ValueError as ve:
        print(f"ValueError as expected for invalid path: {ve}")

# 运行测试
if __name__ == "__main__":
    test_path_check()

