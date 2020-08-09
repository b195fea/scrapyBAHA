import subprocess
from scrapy import cmdline

if __name__ == '__main__':
    # cmdline.execute("scrapy crawl bh3".split())
    cmdline.execute("scrapy crawl bh3 -o bh3-2020-08-10.csv".split())
    # subprocess.run('scrapy crawl bh3')
    # print(t.getName())