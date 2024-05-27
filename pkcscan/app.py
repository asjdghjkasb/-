# 第三方库
import requests
from requests.exceptions import HTTPError, RequestException
# 自定义库
from core.initialize import globals
from core.initialize import system
from core.bin import core
from core.initialize.printf import printfa
from core.initialize.printf import printToConsole
from core.initialize.printf import printToFile
from core.bin.OInitializeURL import OInitializeURL


def app():
    """
    此函数是整个程序的主题,用于上下衔接各个方法
    """
    ObaseURL = OInitializeURL(globals.get_value("BaseURL_Path"))  # 将输入的BaseURL_Path加载至OInitializeURL类中
    printfa("[*] 正在进行被动指纹识别", "message")
    
    try:
        response = requests.get(ObaseURL.url)
        response.raise_for_status()  # 检查HTTP响应状态码是否是200 (成功)
    except HTTPError as http_err:
        printfa(f"HTTP error occurred: {http_err}", "red")  # HTTP错误
    except RequestException as req_err:
        printfa(f"Request error occurred: {req_err}", "red")  # 其他请求错误
    except Exception as err:
        printfa(f"An error occurred: {err}", "red")  # 其他非请求相关错误
    else:
        core.passiveFingerprintMatching(response)  # 继续处理响应数据
