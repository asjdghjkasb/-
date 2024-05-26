import json
import os
import sys
from module.Poc.fingerprint import NmapPortScanner
from module.Poc.loadPoc import PocLoader
from module.Poc.execUPoc import GetPocExecutor, PostPocExecutor

# 基础目录路径设置，用于加载模块等
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

"""
/**
* 解析端口范围输入。
*
* @param port_input 用户输入的端口范围，例如 "100-200"。
* @return 返回一个端口范围的元组 (start_port, end_port)，如果输入不是范围则返回相同的端口号。
* @throws ValueError 如果输入格式不正确或起始端口大于结束端口。
*/
"""


def parse_port_range(port_input):
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
            pass
    try:
        return int(port_input), int(port_input)
    except ValueError:
        raise ValueError("Invalid port range or port number.")


"""
/**
* 主应用程序入口。
*
* @param directory_path 存放POC脚本的目录路径。
*/
"""


def app(directory_path):
    while True:
        # 欢迎信息与URL输入
        print("Welcome to the pKcScan!")
        url = input("Please enter the IP address (default_port:80): ")

        # 解析IP地址和端口号
        if ":" in url:
            parts = url.split(':')
            ip = parts[0]
            port = int(parts[1].split('/')[0])
        else:
            ip = url
            port = 80

        try:
            # 扫描端口信息
            port_scanner = NmapPortScanner()
            fingerprints = port_scanner.print_port_info(ip, port)
            parsed_data = json.loads(fingerprints)
            if fingerprints:
                print(
                    f"{url}\t服务: {parsed_data[0]['product']} {parsed_data[0]['version']}\t操作系统：{parsed_data[0]['os']}\t指纹：{parsed_data[0]['finger']}")
            else:
                print("An error occurred while scanning.")
                break

            # 加载并执行相应的POC
            poc_loader = PocLoader(directory_path)
            pocs = poc_loader.load_pocs(parsed_data[0]['finger'])

            executors = {
                'get': GetPocExecutor(),
                'post': PostPocExecutor()
            }

            results = []
            for poc in pocs:
                method = poc['request']['method'].lower()
                executor = executors.get(method)
                if executor:
                    result = executor.execute(ip, port, poc)
                    results.append(result)
                    print(f"Result for {poc['request']['url']}: {result}")
                else:
                    print(f"[-] Unsupported method {method} in POC")

            # 输出POC执行结果
            if results:
                print("POC Results:")
                for result in results:
                    print(result)
            else:
                print("No results or no POCs executed.")

        except Exception as e:
            print("An error occurred:", str(e))
