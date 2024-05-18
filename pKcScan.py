# 导入core/initialize 模块
from core.initialize.flag import banner
print(banner())
from core.initialize import globals
from core.initialize import system
from core.bin.scanner import app

# _global_dict 全局参数只允许在这个文件中改动
def initialize():
    globals.init()
    globals.set_value("SYS_OS", system.os_check()) # 当前操作系统
    globals.set_value("SYS_Path", system.path_check(globals.get_value("SYS_OS"))) # 当前绝对路径



app()
