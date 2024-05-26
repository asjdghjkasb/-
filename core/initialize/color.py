# 导入 colorama 模块用于控制台输出的颜色
from colorama import init
from colorama import Fore, Back, Style, Cursor

# 初始化 colorama，设置 autoreset=True 以便在每次输出后重置颜色设置
init(autoreset=True)

# 定义 Colored 类，用于提供各种颜色的字符串输出方法
class Colored:
    @staticmethod
    def magenta(s):
        # 返回亮紫色字符串
        return Style.BRIGHT + Fore.MAGENTA + s + Fore.RESET + Style.RESET_ALL

    @staticmethod
    def green(s):
        # 返回亮绿色字符串
        return Style.BRIGHT + Fore.GREEN + s + Fore.RESET + Style.RESET_ALL

    @staticmethod
    def white(s):
        # 返回白色字符串
        return Fore.WHITE + s + Fore.RESET + Style.RESET_ALL

    @staticmethod
    def cyan(s):
        # 返回亮青色字符串
        return Style.BRIGHT + Fore.CYAN + s + Fore.RESET + Style.RESET_ALL

    @staticmethod
    def cyan_fine(s):
        # 返回青色字符串
        return Fore.CYAN + s + Fore.RESET + Style.RESET_ALL

    @staticmethod
    def yellow(s):
        # 返回亮黄色字符串
        return Style.BRIGHT + Fore.YELLOW + s + Fore.RESET + Style.RESET_ALL

    @staticmethod
    def red(s):
        # 返回亮红色字符串
        return Style.BRIGHT + Fore.RED + s + Fore.RESET + Style.RESET_ALL
    
    @staticmethod
    def green_message():
        return Style.BRIGHT + Fore.GREEN + "[Message]" + Fore.RESET + Style.RESET_ALL

    @staticmethod
    def yel_info():
        # 返回亮黄色的 "[INFO]" 标签字符串
        return Style.BRIGHT + Fore.YELLOW + "[INFO]" + Fore.RESET + Style.RESET_ALL

    @staticmethod
    def red_warn():
        # 返回亮红色的 "[WARN]" 标签字符串
        return Style.BRIGHT + Fore.RED + "[WARN]" + Fore.RESET + Style.RESET_ALL
    
    @staticmethod
    def cyan_input():
        # 返回亮红色的 "[WARN]" 标签字符串
        return Style.BRIGHT + Fore.RED + "[input]" + Fore.RESET + Style.RESET_ALL

# 创建 Colored 类的实例
color = Colored()

# 测试 Colored 类的输出
def test_colored():
    color = Colored()
    
    print(color.magenta("This is magenta"))
    print(color.green("This is green"))
    print(color.white("This is white"))
    print(color.cyan("This is cyan"))
    print(color.cyan_fine("This is cyan fine"))
    print(color.yellow("This is yellow"))
    print(color.red("This is red"))
    print(color.yel_info() + " This is an info message")
    print(color.red_warn() + " This is a warning message")

if __name__ == "__main__":
    test_colored()