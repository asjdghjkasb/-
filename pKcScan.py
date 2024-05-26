import os
import sys
from core.initialize.flag import banner
print(banner())
from core.initialize import globals
from core.initialize import system
from core.bin.scanner import app

# _global_dict 全局参数只允许在这个文件中改动
def initialize():
    globals.init()
    globals.set_value("SYS_OS", system.os_check()) # 当前操作系统
    globals.set_value("SYS_Path", os.path.abspath(os.path.dirname(__file__))) # 当前绝对路径
    sys.path.append(globals.get_value("SYS_Path")) # 添加项目根目录到环境变量
    globals.set_value("Poc_Path", system.path_add(globals.get_value("SYS_Path"), "module", "Poc", "pikachuPoc")) # Poc路径

if __name__ == "__main__":
    initialize()
    print(globals.get_all_items())
    poc_path = globals.get_value("Poc_Path")
    app(poc_path)
