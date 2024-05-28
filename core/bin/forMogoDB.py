from core.initialize import globals

mongodb=globals.GlobalObjectStore.get_object("Omongo")

def get_all_fingerprints(): # 查询所有数据
    mongodb = globals.GlobalObjectStore.get_object("Omongo")
    # print("MongoDB object:", mongodb)
    if mongodb is None:
        print("Database connection is not initialized")
        return []

    # print("Database connection is initialized")

    try:
        collection = mongodb["FingerPrint"]
        fingerprints = list(collection.find({}, {"_id": 0})) 
        # print("Fingerprints:", fingerprints)
        return fingerprints
    except Exception as e:
        print("Error occurred while querying database:", e)
        return []

def get_all_fingerprints_with_empty_method(): # 查询所有请求方法为空的
    mongodb = globals.GlobalObjectStore.get_object("Omongo")
    if mongodb is None:
        print("Database connection is not initialized")
        return []

    try:
        collection = mongodb["FingerPrint"]
        # 查询 mainRequest 中 method 字段为空的文档
        fingerprints = list(collection.find({"mainRequest.1.request.method": ""}, {"_id": 0}))
        if fingerprints:
            return fingerprints
    except Exception as e:
        print("Error occurred while querying database:", e)
        return []


def get_all_poc():
    """
    查询所有Poc数据
    """
    mongodb = globals.GlobalObjectStore.get_object("Omongo")
    if mongodb is None:
        print("Database connection is not initialized")
        return []
    try:
        collection = mongodb["Poc"]
        fingerprints = list(collection.find({}, {"_id": 0}))
        return fingerprints
    except Exception as e:
        print("Error occurred while querying database:", e)
        return []

def get_poc_by_name(poc_name):
    """
    根据名称查询Poc数据
    :param poc_name: Poc名称
    :return: 匹配的Poc数据或空列表
    """
    mongodb = globals.GlobalObjectStore.get_object("Omongo")
    if mongodb is None:
        print("Database connection is not initialized")
        return []
    try:
        collection = mongodb["Poc"]
        pocs = list(collection.find({"name": poc_name}, {"_id": 0}))
        if pocs:
            return pocs
        else:
            print(f"No Poc found with the name: {poc_name}")
            return []
    except Exception as e:
        print(f"Error occurred while querying database: {e}")
        return []

# 示例用法
if __name__ == "__main__":
    fingerprints = get_all_fingerprints()
    print(f"Retrieved {len(fingerprints)} fingerprints")
    for fingerprint in fingerprints:
        print(fingerprint)
