from abc import ABC, abstractmethod
from urllib.parse import quote, urlparse, urlunparse
import requests


# 定义一个抽象基类，用于执行PoC（Proof of Concept）测试。
class PocExecutor(ABC):
    @abstractmethod
    def execute(self, ip, port, jsonData):
        """
        执行PoC测试的抽象方法。

        :param ip: 目标IP地址。
        :param port: 目标端口号。
        :param jsonData: 包含请求和响应信息的JSON数据。
        :return: 执行结果，可以是漏洞存在与否的消息或其他信息。
        """
        pass


# GET请求PoC执行器，具体实现execute方法。
class GetPocExecutor(PocExecutor):
    def execute(self, ip, port, jsonData):
        """
        执行GET请求的PoC测试。

        :param ip: 目标IP地址。
        :param port: 目标端口号。
        :param jsonData: 包含请求和响应信息的JSON数据。
        :return: 执行结果，可以是漏洞存在与否的消息或其他信息。
        """
        url = jsonData['request']['url']
        payload = jsonData['request']['requestbody']
        check_response = jsonData['response']['responsebody']
        method = jsonData['request']['method']

        # 处理GET请求的参数拼接。
        if method.lower() == 'get':
            if '?' in url:
                query_params = url.split('?')[1]
                if '&' in query_params:
                    rest = query_params.split('&', 1)[1]
                    rest = f'&{rest}'
                    param_name = query_params.split('=')[0]
                else:
                    param_name = query_params.split('=')[0]
                    rest = ''

                encoded_payload = quote(payload, safe='')
                parsed_url = urlparse(url)
                new_netloc = f"{ip}:{port}"
                query = ""
                new_url = urlunparse(parsed_url._replace(netloc=new_netloc, query=query))
                test_url = f"{new_url}?{param_name}={encoded_payload}{rest}"

                try:
                    response = requests.get(test_url)
                    # 检查响应结果。
                    if response.status_code == 200:
                        if check_response in response.text:
                            return jsonData['response']['statusmessage']
                        else:
                            return "[-] 不存在漏洞"
                    else:
                        return f"[-] Non-200 response code: {response.status_code}"
                except Exception as e:
                    return f"[-] Error fetching {test_url}: {e}"
            else:
                return "[-] No query parameters in the URL"
        return "[-] Unsupported method"


# POST请求PoC执行器，具体实现execute方法。
class PostPocExecutor(PocExecutor):
    def execute(self, ip, port, jsonData):
        """
        执行POST请求的PoC测试。

        :param ip: 目标IP地址。
        :param port: 目标端口号。
        :param jsonData: 包含请求和响应信息的JSON数据。
        :return: 执行结果，可以是漏洞存在与否的消息或其他信息。
        """
        url = jsonData['request']['url']

        # 重构URL，去除参数部分。
        parsed_url = urlparse(url)
        new_netloc = f"{ip}:{port}"
        query = ""
        new_url = urlunparse(parsed_url._replace(netloc=new_netloc, query=query))

        # 设置请求头和请求体。
        headers = jsonData['request']['requestheader']
        cookies = {'PHPSESSID': jsonData['request']['cookie']}
        data = jsonData['request']['requestbody']

        try:
            response = requests.post(new_url, headers=headers, cookies=cookies, data=data)
            # 检查响应结果。
            if response.status_code == 200:
                if jsonData['response']['responsebody'] in response.text:
                    return jsonData['response']['statusmessage']
                else:
                    return "[-] 不存在漏洞"
            else:
                return f"[-] 非200响应码: {response.status_code}"
        except Exception as e:
            return f"[-] 请求失败: {e}"
