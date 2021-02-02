import pymongo

# def find(dblist):
    # mycol = dblist["zjh2"]
    # collist = mycol.list_collection_names()
    # for item in collist:
    #     print(item)

if __name__ == '__main__':
    try:
        conn = pymongo.MongoClient('mongodb://localhost:27017/')
        db = conn.zjh
        collection = db.zjh
        # cursor = collection.find({})
        # data = [d for d in cursor]
        # print(data)
        # print(data[0])

        collection.insert_one({"name":"鍾嘉豪"})
        # cursor = collection.find({})
        # data = [d for d in cursor]
        # print(data)
        #
        # collection.delete_one({"name":"鍾嘉豪"})
        # cursor = collection.find({})
        # data = [d for d in cursor]
        # print(data)

    except Exception as e:
        print("發生錯誤：" + e)








