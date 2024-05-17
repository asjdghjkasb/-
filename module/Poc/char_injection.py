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
                return "[+] Potential SQL Injection Detected with Payload: %s" % payload
                # print(f"[+] Response: {response.text}")  
            else:  
                return "[-] No clear signs of SQL Injection with Payload: %s" % payload
                # 你也可以记录或打印完整的响应，以便后续分析  
        else:  
            return "[-] Non-200 response code: {response.status_code}"  
    except Exception as e:  
        return "[-] Error fetching {test_url}: {e}" 
