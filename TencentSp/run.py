from scrapy.cmdline import execute
import time
import os


def scr():
    while True:
        print('开始爬去')
        os.system('scrapy crawl tencentPostion')
        time.sleep(60)  #每隔一天运行一次 24*60*60=86400s


if __name__ == '__main__':
    scr()
