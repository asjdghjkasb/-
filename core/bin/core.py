# 读取对象PocData并形成数据包结构,使其能正常发送
from core.bin.Oreadjson import PocData
from core.bin.Oreadjson import RequestResponse
from core.bin.OInitializeURL import OInitializeURL
from requests.exceptions import HTTPError, RequestException
from core.initialize import globals
import requests
from core.initialize.printf import printfa
from core.initialize.printf import printToConsole
from core.initialize.printf import printToFile

# 被动指纹匹配
def passiveFingerprintMatching(response,allFingerprintOPocData):
    """
    被动指纹匹配
    :param PocData: PocData对象
    :return: 匹配结果
    """
    for fingerOPocData in allFingerprintOPocData:
        requestResponse=fingerOPocData.get_main_request_by_key("1")#获取第一个请求包
        if requestResponse.response_body in response.text:
            printfa(f"识别到指纹为{fingerOPocData.name}","info")
            return fingerOPocData.name
        

def switchexecPoc(type,fingerOPocData):
    switch = {
        "1": tpye1execPoc(fingerOPocData),
        "2": tpye2execPoc(fingerOPocData)
    }
    return switch.get(type, "错误的Poc类型")

def tpye1execPoc(fingerOPocData):
    """
    执行指定的Poc测试
    :param fingerOPocData: Poc数据对象
    :return: 返回0表示未发现漏洞或发生错误
    """
    ObaseURL = OInitializeURL(globals.get_value("BaseURL_Path"))  # 加载一个基础Url
    PocORequestResponse = fingerOPocData.get_main_request_by_key("1")
    Url = OInitializeURL(PocORequestResponse.request_path)
    
    if not PocORequestResponse.request_method:
        printfa(f"存在一条错误Poc：关键信息 {fingerOPocData.name}: {fingerOPocData.vuln}")
        return "0"
    
    if PocORequestResponse.request_path:
        ObaseURL.path = Url.path
        ObaseURL.query = Url.query
    else:
        ObaseURL.path = ""
        ObaseURL.query = ""
    
    cookies = PocORequestResponse.request_cookie or {}
    headers = PocORequestResponse.request_header or {}
    
    try:
        printfa(f"正在检测是否存在 {fingerOPocData.vuln}", "message")
        
        if PocORequestResponse.request_method.upper() == "GET":
            response = requests.get(ObaseURL.url, cookies=cookies, headers=headers)
        elif PocORequestResponse.request_method.upper() == "POST":
            data = PocORequestResponse.request_body or {}
            response = requests.post(ObaseURL.url, cookies=cookies, headers=headers, data=data)
        else:
            printfa(f"不支持的请求方法：{PocORequestResponse.request_method}", "red")
            return "0"
        
        response.raise_for_status()  # 检查HTTP响应状态码是否是200 (成功)
        
    except HTTPError as http_err:
        printfa(f"HTTP error occurred: {http_err}", "red")  # HTTP错误
        return "0"
    except RequestException as req_err:
        printfa(f"Request error occurred: {req_err}", "red")  # 其他请求错误
        return "0"
    except Exception as err:
        printfa(f"An error occurred: {err}", "red")  # 其他非请求相关错误
        return "0"
    else:
        if PocORequestResponse.response_body in response.text:
            printfa(f"网址 '{ObaseURL.scheme}://{ObaseURL.netloc}' 指纹识别为 {fingerOPocData.name} 发现存在: {fingerOPocData.vuln}\n","cyan")
        else:
            printfa(f"未发现 {fingerOPocData.vuln}")

def tpye2execPoc(fingerOPocData):
    return 2