import os
import sys

from core.initialize.flag import banner
print(banner())
from core.initialize import globals
from core.initialize import system
from core.initialize import mongoConnect
from core.bin import writeJsonToDB
from core.initialize.printf import printfa
from core.initialize.printf import printToConsole
from core.initialize.printf import printToFile
from pkcscan.app import app

# _global_dict 全局参数只允许在这个文件中改动
def initialize():# 初始化
    globals.init()
    globals.set_value("SYS_OS", system.os_check()) # 当前操作系统
    globals.set_value("SYS_Path", os.path.abspath(os.path.dirname(__file__))) # 当前绝对路径
    sys.path.append(globals.get_value("SYS_Path")) # 添加项目根目录到环境变量
    globals.set_value("Poc_Path", system.path_add(globals.get_value("SYS_Path"), "module", "Poc")) # Poc路径
    globals.set_value("Fingerprint_Path", system.path_add(globals.get_value("SYS_Path"), "module", "fingerprint","allFingerprint")) # fingerprint路径
    globals.set_value("Report_Path", system.path_add(globals.get_value("SYS_Path"), "module", "Report",f"{system.get_time()}.md")) # 报告路径
    printToConsole(f"此次扫描生成报告位置为:\n{globals.get_value('Report_Path')}", "message")
    globals.set_value("CONFIG_FILE_PATH", system.path_add(globals.get_value("SYS_Path"), "core", "initialize","config.json")) # 初始化配置路径
    writeJsonToDB.initialize()# 第一次使用时初始化数据库
    mongo_connector_module = mongoConnect.MongoConnector(host='localhost', port=27017, db_name='module')#这里连接数据库
    mongo_connector_module.connect()
    mongoModuledb=mongo_connector_module.get_database('module')
    globals.GlobalObjectStore.set_object("Omongo",mongoModuledb)# 将数据库连接对象放入全局参数中
    printToConsole("请输入目标URL:","info")
    globals.set_value("BaseURL_Path",input())# 目标URl
    printToFile(f"初始化完成,当前时间为:{system.get_time()},全局变量为:\n{globals.print_all_globals()}",globals.get_value("Report_Path"))

if __name__ == "__main__":
    initialize()
    app()
    globals.GlobalObjectStore.get_object("Omongo").client.close()
    printfa("数据库已断开","message")