from core.initialize import globals
from core.initialize import system
import module.Poc.fingerprint as fingerprint
import OreadPocJson

def fingerToPoc(finger):
    if not finger:
        raise ValueError("指纹不能为空")

    poc_path = system.path_add(globals.get_value("Poc_Path"), finger)
    if system.path_check(poc_path):
        return poc_path
    else:
        return "库中没有该指纹Poc"
    
def test_fingerToPoc():
    #测试存在的指纹
    finger = "pikachu"
    try:
        result = fingerToPoc(finger)
        print(result)
        assert result == r"C:\Users\8612\Desktop\Vulnerability-scanning\module\Poc\pikachu", f"Test failed for existing finger: {result}"
        print(f"fingerToPoc('{finger}') passed: {result}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RuntimeError as re:
        print(f"RuntimeError: {re}")
    except AssertionError as ae:
        print(ae)

    # 测试不存在的指纹
    finger = "non_existing_finger"
    try:
        result = fingerToPoc(finger)
        assert result == "库中没有该指纹Poc", f"Test failed for non-existing finger: {result}"
        print(f"fingerToPoc('{finger}') passed: {result}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RuntimeError as re:
        print(f"RuntimeError: {re}")
    except AssertionError as ae:
        print(ae)

    # 测试空指纹
    finger = ""
    try:
        fingerToPoc(finger)
    except ValueError as ve:
        print(f"ValueError as expected: {ve}")

# 运行测试
if __name__ == "__main__":
    test_fingerToPoc()