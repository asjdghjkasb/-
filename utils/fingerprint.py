import nmap  
import json  
  
def print_port_info(ip):  
    nm = nmap.PortScanner()  
    try:  
        # 扫描IP地址，扫描所有端口并尝试获取服务版本信息  
        nm.scan(hosts=ip, arguments='-O -sV -p-')  
  
        # 检查扫描结果中是否包含该IP地址  
        if ip in nm.all_hosts():  
            # 初始化一个空列表来存储端口信息  
            open_ports = []  
            # 提取TCP端口信息  
            for port, info in nm[ip]['tcp'].items():  
                # 端口信息可能包括多个状态（例如，open, closed, filtered等）  
                if info['state'] == 'open':   
                    product = info.get('product')  
                    version = info.get('version')  
                    if product and version:  
                        open_ports.append({  
                            'port': port,  
                            'product': product,  
                            'version': version  
                        })  
            # 将端口信息列表转换为JSON字符串  
            json_data = json.dumps(open_ports, indent=4)  
            return json_data  
        else:  
            return json.dumps([], indent=4)  # 如果IP地址不存在于扫描结果中，返回一个空列表的JSON  
    except nmap.PortScannerError as e:  
        print(f"Nmap scan error: {e}")  
        return json.dumps({'error': str(e)}, indent=4)  # 返回包含错误的JSON  
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")  
        return json.dumps({'error': str(e)}, indent=4)  # 返回包含未知错误的JSON  