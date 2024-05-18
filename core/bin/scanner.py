import json
import sys,os

# 获取项目根目录（假设你的脚本在 bin 目录下）  
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir) 

from module.Poc import loadPoc
from module.Poc import fingerprint
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

def app(): 
    while(1): 
        print("Welcome to the pKcScan!")    
        url = input("Please enter the IP address(default_port:80): ")

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
        parsed_data = json.loads(fingerprints) 
        if fingerprints is not None:  
            print(url + "\t服务:" + parsed_data[0]['product'] + ' ' + parsed_data[0]['version'] + '\t操作系统：' + parsed_data[0]['os'] + '\t指纹：' + parsed_data[0]['finger'])  
        else:  
            print("An error occurred while scanning.")
            break
        result = loadPoc.load_poc(parsed_data[0]['finger'])
        print(result)

        # result = char_injection.sql_injection_check(url,payload)
        # print(result)  
