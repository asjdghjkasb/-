# 该脚本用于统一管理输出，并形成报告(日志)
import os
import errno
# 从 core.initialize 导入 color 对象
from core.initialize.color import color
from core.initialize import globals

def printToConsole(msg, color_name='normal'):
    """
    打印消息到控制台，并根据指定的颜色进行着色
    :param msg: 要打印的消息
    :param color_name: 指定的颜色名称，默认为 'normal'
    """
    if not isinstance(msg, str):
        try:
            msg = str(msg)
        except Exception as e:
            print("Error converting message to string:", e)
            return

    if color_name == 'magenta':
        print(color.magenta(msg))
    elif color_name == 'green':
        print(color.green(msg))
    elif color_name == 'white':
        print(color.white(msg))
    elif color_name == 'cyan':
        print(color.cyan(msg))
    elif color_name == 'cyan_fine':
        print(color.cyan_fine(msg))
    elif color_name == 'yellow':
        print(color.yellow(msg))
    elif color_name == 'red':
        print(color.red(msg))
    elif color_name == 'info':
        print(color.yel_info() + " " + msg)
    elif color_name == 'warn':
        print(color.red_warn() + " " + msg)
    elif color_name == 'message':
        print(color.green_message() + " " + msg)
    elif color_name == 'input':
        print(color.cyan_input() + " " + msg)
    else:
        print(msg)


def printToFile(msg, file_path=None):
    """
    将消息写入文件
    :param msg: 要写入的消息
    :param file_path: 文件路径，默认为 Report_Path
    """
    if file_path is None:
        file_path = globals.get_value("Report_Path")

    if not isinstance(msg, str):
        try:
            msg = str(msg)
        except Exception as e:
            print("Error converting message to string:", e)
            return

    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(msg + '\n')
    except FileNotFoundError:
        # 如果文件不存在，创建文件并写入消息
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as e:
            if e.errno != errno.EEXIST:
                # 如果创建文件夹失败，打印错误信息
                print("Failed to create directory:", os.path.dirname(file_path))
                print("Error:", e)
                return
        # 创建文件后再次尝试写入消息
        try:
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(msg + '\n')
        except Exception as e:
            # 如果写入消息失败，打印错误信息
            print("Failed to write to file:", file_path)
            print("Error:", e)

def printfa(msg, color_name='normal'):
    """
    打印消息到控制台和文件，并根据指定的颜色进行着色
    :param msg: 要打印的消息
    :param color_name: 指定的颜色名称，默认为 'normal'
    """
    printToConsole(msg, color_name)
    printToFile(msg, globals.get_value("Report_Path"))


def test():
    printToConsole("This is a normal message")
    printToConsole("This is a magenta message", "magenta")
    printToConsole("This is a green message", "green")
    printToConsole("This is a white message", "white")
    printToConsole("This is a cyan message", "cyan")
    printToConsole("This is a cyan fine message", "cyan_fine")
    printToConsole("This is a yellow message", "yellow")
    printToConsole("This is a red message", "red")
    printToConsole("This is an info message", "info")
    printToConsole("This is a warning message", "warn")
    printToConsole("This is a custom message", "message")
