import nmap
import json
import requests
import core.data.config.config as config


class PortScannerInterface:
    """
    端口扫描器接口类，定义了端口信息打印的方法。
    """

    def print_port_info(self, ip, port=80):
        """
        打印指定IP地址和端口的信息。

        参数:
        - ip: str，目标IP地址。
        - port: int，目标端口号，默认为80。
        """
        pass


class NmapPortScanner(PortScannerInterface):
    """
    使用nmap进行端口扫描的实现类，继承自PortScannerInterface。
    """

    def print_port_info(self, ip, port=80):
        """
        打印指定IP地址和端口的信息，包括端口状态、服务版本和操作系统指纹等。

        参数:
        - ip: str，目标IP地址。
        - port: int，目标端口号，默认为80。

        返回:
        - str，端口扫描结果的JSON字符串。
        """
        finger = 'unknown'  # 初始化服务器指纹为未知

        # 尝试通过HTTP请求匹配服务器指纹
        for finger_candidate in config.fingerprints:  # conf是未定义的变量，假设为配置文件或字典
            url = f'http://{ip}:{port}'
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    if finger_candidate.lower() in response.text.lower():
                        finger = finger_candidate
                        break  # 找到匹配的指纹后跳出循环

            except requests.RequestException as e:
                print(f"Request failed: {e}")
                continue  # 请求失败时继续尝试其他指纹匹配

        # 使用nmap进行端口扫描并获取服务版本信息
        nm = nmap.PortScanner()
        try:
            arguments = '-O -sV -p {}'.format(port)  # 构造nmap扫描参数
            nm.scan(hosts=ip, arguments=arguments)  # 执行扫描

            if ip in nm.all_hosts():
                open_ports = []  # 用于存储打开的端口信息
                if 'tcp' in nm[ip]:
                    info = nm[ip]['tcp']
                    if info[port]['state'] == 'open':  # 如果端口是打开的
                        product = info[port]['product']
                        version = info[port]['version']
                        OS = info[port]['extrainfo']
                        if product and version:  # 如果产品和版本信息都可用
                            open_ports.append({
                                'product': product,
                                'version': version,
                                'os': OS,
                                'finger': finger  # 添加服务器指纹信息
                            })
                json_data = json.dumps(open_ports, indent=4)  # 将结果转换为JSON字符串
                return json_data
            else:
                return json.dumps([], indent=4)  # 如果没有发现主机，返回空JSON数组
        except nmap.PortScannerError as e:
            # 处理nmap扫描错误
            print(f"Nmap scan error: {e}")
            return json.dumps({'error': str(e)}, indent=4)
        except Exception as e:
            # 处理其他意外错误
            print(f"An unexpected error occurred: {e}")
            return json.dumps({'error': str(e)}, indent=4)
