import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


# 扫描单个端口的函数
def scan_port(ip, port):
    """
    尝试连接给定IP地址的指定端口，以检测端口是否开放。

    参数:
    - ip: 目标IP地址，字符串类型。
    - port: 要扫描的端口号，整数类型。

    返回值:
    - 一个元组，包含端口号和一个布尔值，表示端口是否开放（True为开放，False为关闭）。
    """
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
    """
    并发扫描指定IP地址的一系列端口，以确定哪些端口是开放的。

    参数:
    - ip: 要扫描的IP地址，字符串类型。
    - start_port: 扫描的起始端口号，整数类型，默认为1。
    - end_port: 扫描的结束端口号，整数类型，默认为65535。
    - max_workers: 线程池中最大工作线程数，整数类型，默认为100。

    返回值:
    - 一个字典，键为扫描的端口号，值为布尔值，表示端口是否开放（True为开放，False为关闭）。
    """
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交任务到线程池
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]

        # 使用as_completed来非阻塞地获取结果
        results = {}
        for future in as_completed(futures):
            port, open_status = future.result()
            results[port] = open_status

    return results
