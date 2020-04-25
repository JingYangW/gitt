1

# def test(info):
#     if info.username == "root" and info.password == "1223":
#         print("你有权限")
#     else:
#         print("你没权限")
#         return
#     return "123"
#
#
# def test2(info):
#     if info.username == "root" and info.password == "1223":
#         print("你有权限")
#     else:
#         print("你没权限")
#         return
#     return "456"
#
#
# def permit(func):
#     def identify(info):
#         if info.username == "root" and info.password == "1223":
#             print("permit")
#             return func(info)
#         else:
#             print("用户名密码错误")
#             return
#     return identify
#
#
# @permit
# def test(info):
#     return "123"
#
#
# @permit
# def test2(info):
#     return "456"
#
#
# if __name__ == "__main__":
#     print(test(info))
#     print(test2(info))


2

import os


# os.path.isdir()和os.path.isfile()需要传入的参数是绝对路径，但是os.listdir()返回的只是一个某个路径下的文件和列表的名称.
#
# 常见错误：直接使用os.listdir()的返回值当做os.path.isdir()和os.path.isfile()的入参
#
# 正确用法：需要先使用python路径拼接os.path.join()函数，将os.listdir()返回的名称拼接成文件或目录的绝对路径再传入os.path.isdir()和os.path.isfile().

# def lisall(path):
#     dir = os.listdir(path)
#     for f in dir:
#         # print(f)
#         fuldir = os.path.join(path, f)
#         # print(fuldir)
#         if os.path.isdir(fuldir):
#             print("路径" + fuldir)
#         if os.path.isfile(fuldir):
#             print("文件" + fuldir)
#
#
# if __name__ == "__main__":
#     lisall(r"D:\jenkins")
#
#


# def zuida(path):
#     dir = os.walk(path)
#     a = 0
#     for dirpath, dirname, filenames in dir:
#         for filename in filenames:
#             fuldir = os.path.join(dirpath, filename)
#             b = os.path.getsize(fuldir)
#             if b>a:
#                 a = b
#             # 遍历所有文件
#                 print(a)
#     print(a)
#     print(fuldir)
#
#
# if __name__ == "__main__":
#     zuida(r"D:\jenkins")
