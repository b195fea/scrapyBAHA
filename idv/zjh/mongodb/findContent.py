from pymongo import MongoClient

if __name__ == '__main__':
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient["bh3_scrapy"]
    mycol = mydb["bh3_2"]

    # content = mycol.find_one()["C03_content"]

    content = ""
    for x in mycol.find():
        content = content + x["C03_content"]

    print(content)
    filename = 'bh3_content.txt'
    with open(filename, 'wb') as f:
        f.write(content.encode())
        f.close();