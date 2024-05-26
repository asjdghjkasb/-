import os
import sys
from core.initialize.flag import banner
print(banner())
from core.initialize import globals
from core.initialize import system
from core.initialize.printf import printfa
from core.initialize.printf import printToConsole

# _global_dict 全局参数只允许在这个文件中改动
def initialize():# 初始化
    globals.init()
    globals.set_value("SYS_OS", system.os_check()) # 当前操作系统
    globals.set_value("SYS_Path", os.path.abspath(os.path.dirname(__file__))) # 当前绝对路径
    sys.path.append(globals.get_value("SYS_Path")) # 添加项目根目录到环境变量
    globals.set_value("Poc_Path", system.path_add(globals.get_value("SYS_Path"), "module", "Poc")) # Poc路径
    globals.set_value("Report_Path", system.path_add(globals.get_value("SYS_Path"), "module", "Report",f"{system.get_time()}.md")) # 报告路径
    printToConsole(f"此次扫描生成报告位置为:\n{globals.get_value('Report_Path')}", "message")

    
if __name__ == "__main__":
    initialize()

    

