from core.initialize import globals

mongodb=globals.GlobalObjectStore.get_object("Omongo")

def get_all_fingerprints():
    mongodb = globals.GlobalObjectStore.get_object("Omongo")
    # print("MongoDB object:", mongodb)
    if mongodb is None:
        print("Database connection is not initialized")
        return []

    # print("Database connection is initialized")

    try:
        collection = mongodb["FingerPrint"]
        fingerprints = list(collection.find({}, {"_id": 0}))  # 查询所有数据，并排除 _id 字段
        # print("Fingerprints:", fingerprints)
        return fingerprints
    except Exception as e:
        print("Error occurred while querying database:", e)
        return []



# 示例用法
if __name__ == "__main__":
    fingerprints = get_all_fingerprints()
    print(f"Retrieved {len(fingerprints)} fingerprints")
    for fingerprint in fingerprints:
        print(fingerprint)
