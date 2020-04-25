# # 1 使用多线程写一个并发http get请求的程序 可设置并发数和请求总数，返回请求状态码
# import threading
# import requests
#
#
# def httpgetthread(url):
#     res = requests.get(url)
#     print("url：", url, "状态码：", res.status_code)
#
#
# a = ["https://github.com/",
#      "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1",
#      "http://news.baidu.com/",
#      "https://tieba.baidu.com/index.html",
#      "https://www.jianshu.com/",
#      "http://www.51testing.com/html/index.html"
#      ]
# if __name__=="__main__":
#     for i in a:
#         thread = threading.Thread(target=httpgetthread, args=(i,))
#         thread.start()
#         thread.join()

# # 2 使用多进程写一个并发http get请求的程序，可设置并发数和请求总数，返回请求状态码
# import os
# import requests
# from multiprocessing import Process
#
#
# def httpgetprocess(url):
#     res = requests.get(url)
#     print("url:", url, "状态码:", res.status_code)
#
#
# b = ["https://github.com/",
#      "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1",
#      "http://news.baidu.com/",
#      "https://tieba.baidu.com/index.html",
#      "https://www.jianshu.com/",
#      "http://www.51testing.com/html/index.html"
#      ]
# if __name__ == "__main__":
#     for j in b:
#         pro = Process(target=httpgetprocess, args=(j,))
#         pro.start()
#         pro.join()
