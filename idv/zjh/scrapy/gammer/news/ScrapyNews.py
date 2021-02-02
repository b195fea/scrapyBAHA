import subprocess
from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute("scrapy crawl news".split())
    # cmdline.execute("scrapy crawl bh3 -o bh3-2020-08-11.csv".split())
    # cmdline.execute("scrapy crawl bh3 -o bh3-2020-08-11-test.csv".split())
    # subprocess.run('scrapy crawl bh3')
    # print(t.getName())