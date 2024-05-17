import sys,os

# 获取项目根目录（假设你的脚本在 bin 目录下）  
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir) 

from utils import fingerprint,banner
from vulnerabilities.sql_injection import sql_scanner
def parse_port_range(port_input):  
    # 尝试将输入拆分为起始和结束端口  
    ports = port_input.split('-')  
    if len(ports) == 2:  
        try:  
            start_port = int(ports[0])  
            end_port = int(ports[1])  
            if start_port <= end_port:  
                return start_port, end_port  
            else:  
                raise ValueError("Starting port must be less than or equal to ending port.")  
        except ValueError:  
            pass  # 捕获值错误并继续下面的处理  
    # 如果输入不是有效的范围，则假设它是一个单独的端口号  
    try:  
        return int(port_input), int(port_input)  # 返回单个端口的范围  
    except ValueError:  
        raise ValueError("Invalid port range or port number.") 

if __name__ == "__main__": 
    while(1): 
        print("Welcome to the IP Scanner!")    
        url = input("Please enter the IP address(default_port:80): ")
        payload = input("Please enter the payload: ")

        parts = url.split(':')  
        if len(parts) == 1:  
            ip = parts[0]  
            port = 80  # 默认端口为80  
        if len(parts) == 2:  
            ip = parts[0]  
            port = int(parts[1].split('/')[0]) 
        else:  
            print("无效的地址和端口格式")
            break
        fingerprints = fingerprint.print_port_info(ip,port)  
        if fingerprints is not None:  
            print(fingerprints)  
        else:  
            print("An error occurred while scanning.")
            break
        result = sql_scanner.sql_injection_check(url,payload)
        print(result)  
        # if choice == 3:
        #     ip = input("Please enter the IP address: ")  
        #     port_input = input("Please enter the port number or range (Default: 1-65535): ")  
        #     num_threads = input("Please enter the number of threads (Default: 100): ")
            
            # 解析端口范围  
        # try:  
        #     start_port, end_port = parse_port_range(port_input)  
        # except ValueError as e:  
        #     print(e)  
        #     sys.exit(1)  
            
            # 如果用户没有输入范围，使用默认值  
            # if start_port == end_port:  
            #     result = ipScan.ip_scan(ip, start_port, start_port, int(num_threads))  # 假设num_threads是一个合理的默认值  
            # else:  
            #     result = ipScan.ip_scan(ip, start_port, end_port, int(num_threads))  
            
            # open_port = []
            
            # for port, is_open in result.items():  
            #     if is_open:  
            #         open_port.append(port) 
            
            # if open_port: 
            #     print(f"{ip}开放的端口有：{', '.join(map(str, open_port))}")  
            # else:  
            #     print(f"{ip}没有开放的端口。")
