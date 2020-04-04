
class 通讯录(object):

    def __init__(self):
        self.a = []
        self.j = 1

    def add_record(self):
        i = [] ;
        name = str(input("通讯录姓名 :")).strip()
        phonenumber = str(input("电话号码 :")).strip()
        id = self.j
        i.append(name)
        i.append(phonenumber)
        i.append(id)
        self.a.append(i)
        print("添加成功")

    def query_record(self):
        select_type = int(input("查找类型 1-姓名，2-电话号码，3-id 4-查看全部通讯录:"))
        if select_type == 1:
            name = str(input("请输入姓名 :")).strip()
            for c in range(len(self.a)):
                if self.a[c][0] == name:
                    print (self.a[c][0],self.a[c][1],self.a[c][2])
            else:
                print("姓名输入有误，查找失败")
        elif select_type == 2:
            phoneme = str(input("电话号码 :")).strip()
            for c in range(len(self.a)):
                if self.a[c][1] == phoneme:
                    print(self.a[c][0], self.a[c][1], self.a[c][2])
            else:
                print("电话号码输入有误，查找失败")
        elif select_type == 3:
            idell = int(input("id :"))
            for c in range(len(self.a)):
                if self.a[c][2] == idell:
                    print(self.a[c][0], self.a[c][1], self.a[c][2])
            else:
                print("id输入有误，查找失败")
        elif select_type == 4:
            print(self.a)
        else:
            print("要查找的类型不存在")

    def change_record(self):
        select_type = int(input("修改类型查询 1-姓名，2-电话号码，3-id :"))
        if select_type == 1:
            name = str(input("请输入原始姓名")).strip()
            for c in range(len(self.a)):
                if self.a[c][0] == name:
                    self.a[c][0] = str(input("输入新姓名")).strip()
                    print(self.a[c][0], self.a[c][1], self.a[c][2])
                    print("修改成功")
            else:
                print("原始姓名输入有误，查找失败")
        elif select_type == 2:
            phoneme = str(input("原始电话号码")).strip()
            for c in range(len(self.a)):
                if self.a[c][1] == phoneme:
                    self.a[c][1] = str(input("输入新电话号码")).strip()
                    print(self.a[c][0], self.a[c][1], self.a[c][2])
                    print("修改成功")
            else:
                print("原始电话号码输入有误，查找失败")
        elif select_type == 3:
            idell = int(input("原始id"))
            for c in range(len(self.a)):
                if self.a[c][2] == idell:
                    self.a[c][2] = str(input("输入新id")).strip()
                    print(self.a[c][0], self.a[c][1], self.a[c][2])
                    print("修改成功")
            else:
                print("原始id输入有误，查找失败")
        else:
            print("要修改的类型不存在")

    def delete_record(self):
        select_type = int(input("删除类型查询 1-姓名，2-电话号码，3-id :"))
        if select_type == 1:
            name = str(input("请输入姓名")).strip()
            for c in range(len(self.a)):
                if self.a[c][0] == name:
                    self.a.pop(c)
                    print("删除成功")
                    print(self.a[c][0], self.a[c][1], self.a[c][2])
            else:
                print("姓名输入有误，查找失败")
        elif select_type == 2:
            phoneme = str(input("电话号码")).strip()
            for c in range(len(self.a)):
                if self.a[c][1] == phoneme:
                    self.a.pop(c)
                    print("删除成功")
                    print(self.a[c][0], self.a[c][1], self.a[c][2])
            else:
                print("电话号码输入有误，查找失败")
        elif select_type == 3:
            idell = int(input("id"))
            for c in range(len(self.a)):
                if self.a[c][2] == idell:
                    self.a.pop(c)
                    print("删除成功")
                    print(self.a[c][0], self.a[c][1], self.a[c][2])
            else:
                print("id输入有误，查找失败")
        else:
            print("要删除的类型不存在")

    def execute(self):
        while True:
            option = int(input("输入操作类型 1-添加通讯录 2-查询通讯录 3-修改通讯录 4-删除通讯录 5-退出 其他-重新输入 :"))
            if option == 1:
                self.add_record();self.j=self.j+1
            elif option == 2:
                self.query_record()
            elif option == 3:
                self.change_record()
            elif option == 4:
                self.delete_record()
            elif option == 5:
                break
            else:
                print("重新输入")

if __name__=="__main__":
    a = 通讯录().execute()


