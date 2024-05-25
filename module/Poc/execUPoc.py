from urllib.parse import quote, urlparse, urlunparse  
import requests
  
def exe_poc(ip, port, jsonData):  
    url = jsonData['request']['url']  
    payload = jsonData['request']['requestbody']  
    check_response = jsonData['response']['responsebody']  
    method = jsonData['request']['method']  
    # 针对于get请求
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
            else:  
                # 如果只有一个参数，则直接使用该参数  
                param_name= query_params.split('=')[0]  
                rest = ''  
  
            # 对payload进行URL编码  
            encoded_payload = quote(payload, safe='')  
  
            # 构建测试URL  
            parsed_url = urlparse(url) 
            new_netloc = f"{ip}:{port}"
            query = ""
            new_url = urlunparse(parsed_url._replace(netloc=new_netloc,query=query)) 
            test_url = f"{new_url}?{param_name}={encoded_payload}{rest}"  
            try:  
                response = requests.get(test_url)  
                if response.status_code == 200:  
                    if check_response in response.text:  
                        type = jsonData['response']['statusmessage']
                        return type
                    else:
                        type = "[-] 不存在漏洞"
                        return type
                else:  
                    return "[-] Non-200 response code: {}".format(response.status_code)  
            except Exception as e:  
                return "[-] Error fetching {}: {}".format(test_url, e)  
        else:   
            return "[-] No query parameters in the URL"  
    
    elif method == 'post':    
        url = jsonData['request']['url']  
        parsed_url = urlparse(url)  
        new_netloc = f"{ip}:{port}"  
        query = ""
        new_url = urlunparse(parsed_url._replace(netloc=new_netloc, query=query))  

        headers = jsonData['request']['requestheader']  

        cookies = {'PHPSESSID': jsonData['request']['cookie']}  

        data = jsonData['request']['requestbody']  

        try:  
            response = requests.post(new_url, headers=headers, cookies=cookies, data=data)  
    
            if response.status_code == 200:  
                print(response.text)
                if jsonData['response']['responsebody'] in response.text:  
                    
                    return jsonData['response']['statusmessage']  
                else:  
                    return "[-] 不存在漏洞"  
            else:  
                return f"[-] 非200响应码: {response.status_code}"  
        except Exception as e:  
            return f"[-] 请求失败: {e}"  