import socket  
from concurrent.futures import ThreadPoolExecutor, as_completed  
  
# 扫描单个端口的函数  
def scan_port(ip, port):  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.settimeout(0.5)  
    try:  
        s.connect((ip, port))  
        s.close()  
        return port, True  
    except Exception:  
        return port, False  
  
# 扫描指定IP和端口范围的函数，包含默认值  
def ip_scan(ip, start_port=1, end_port=65535, max_workers=100):  
    with ThreadPoolExecutor(max_workers=max_workers) as executor:  
        # 提交任务到线程池  
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]  
  
        # 使用as_completed来非阻塞地获取结果  
        results = {}  
        for future in as_completed(futures):  
            port, open_status = future.result()  
            results[port] = open_status  
  
    return results  