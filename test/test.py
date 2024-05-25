import requests  
from urllib.parse import urlparse, urlunparse  
import json  
  
# 假设这个函数从某个地方加载了POC的JSON数据  
def load_poc(filename):  
    with open(filename, 'r', encoding='utf-8') as file:  
        return json.load(file)  
  
# 处理POST请求的函数  
def execute_post_poc(ip, port, poc_data):  
    url = poc_data['request']['url']  
    parsed_url = urlparse(url)  
    new_netloc = f"{ip}:{port}"  
    query = ""
    new_url = urlunparse(parsed_url._replace(netloc=new_netloc, query=query))  

    headers = poc_data['request']['requestheader']  

    cookies = {'PHPSESSID': poc_data['request']['cookie']}  

    data = poc_data['request']['requestbody']  

    try:  
        response = requests.post(new_url, headers=headers, cookies=cookies, data=data)  
  
        if response.status_code == 200:  
            print(response.text)
            if poc_data['response']['responsebody'] in response.text:  
                
                return poc_data['response']['statusmessage']  
            else:  
                return "[-] 不存在数字型SQL注入"  
        else:  
            return f"[-] 非200响应码: {response.status_code}"  
    except Exception as e:  
        return f"[-] 请求失败: {e}"  
  
if __name__ == "__main__":   
    poc_data = load_poc(r"C:\Users\87788\Desktop\Vulnerability-scanning\test\poc.json")  
      
    result = execute_post_poc("192.168.207.128", "80", poc_data)  
    print(result)