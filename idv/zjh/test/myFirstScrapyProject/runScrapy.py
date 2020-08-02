import subprocess
from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute("scrapy crawl bh3".split())
    # subprocess.run('scrapy crawl bh3')
    # print(t.getName())