# 多线程简单爬虫
import requests
from bs4 import BeautifulSoup
import queue
import threading

start_page = "http://www.163.com"
domain = "163.com"
url_queue = queue.Queue()
seen = set()
addlock = threading.Lock()

seen.add(start_page)
url_queue.put(start_page)


def sotre(url):
    pass


def extract_urls(url):
    urls = []
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    for e in soup.findAll("a"):
        url = e.attrs.get('href', '#')
        urls.append(url)
    return urls


def execute(url_queue, seen, addlock):
    with addlock:
        while True:

            if not url_queue.empty():

                current_url = url_queue.get()
                print(current_url)
                sotre(current_url)
                for next_url in extract_urls(current_url):
                    if next_url not in seen and domain in next_url:
                        seen.add(next_url)
                        url_queue.put(next_url)
            else:
                break


if __name__ == "__main__":
    threads = []
    for i in range(5):#并发次数
        thread = threading.Thread(target=execute, args=(url_queue,seen,addlock,))#主线程中创建子线程 封装线程
        threads.append(thread)
    for item in threads:
        item.start() #线程开始跑
    for item in threads:
        item.join()# 让主线程等子线程都执行完再退出
