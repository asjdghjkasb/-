from urllib.parse import quote  
import requests  
  
def exe_poc(jsonData):  
    url = jsonData['request']['url']  
    payload = jsonData['payload']  
    check_response = jsonData['response']['responsebody']  
    method = jsonData['request']['method']  
  
    if method == 'get':  
        # 检查URL中是否有查询参数
        if '?' in url:  
            # 拆分URL以获取查询参数部分  
            query_params = url.split('?')[1]  
            # 检查是否包含'&'字符  
            if '&' in query_params:  
                # 如果存在多个参数，找到要替换的参数名  
                rest = query_params.split('&',1)[1]  # 只拆分第一个'&'  
                rest = f'&{rest}'
                param_name = query_params.split('=')[0]  
                base_url = url.split('?')[0]  
            else:  
                # 如果只有一个参数，则直接使用该参数  
                param_name= query_params.split('=')[0]  
                rest = ''  
                base_url = url.split('?')[0]  
  
            # 对payload进行URL编码  
            encoded_payload = quote(payload, safe='')  
  
            # 构建测试URL  
            test_url = f"{base_url}?{param_name}={encoded_payload}{rest}"  
  
            try:  
                response = requests.get(test_url)  
                if response.status_code == 200:  
                    if check_response in response.text:  
                        type = jsonData['type']  
                        return type
                else:  
                    return "[-] Non-200 response code: {}".format(response.status_code)  
            except Exception as e:  
                return "[-] Error fetching {}: {}".format(test_url, e)  
        else:  
            # URL中没有查询参数，无法执行替换  
            return "[-] No query parameters in the URL"  
  
    elif method == 'post':  
        # 对于POST请求，您可以直接发送数据  
        try:  
            response = requests.post(url, data=payload)  
            # 在这里添加对POST请求结果的检查  
            # ...  
            return "[+] POST response received"  # 或者其他适当的响应  
        except Exception as e:  
            return "[-] Error fetching {}: {}".format(url, e)  