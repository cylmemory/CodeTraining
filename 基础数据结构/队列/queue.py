# -*- coding: utf-8 -*-


class Queue():
    def __init__(self):
        self.itms = []

    def is_empty(self):
        return self.itms == []

    def enqueue(self, itm):
        self.itms.insert(0, itm)

    def dequeue(self):
        return self.itms.pop()

    def size(self):
        return len(self.itms)


q = Queue()
q.enqueue('cai')
q.enqueue('yu')
q.enqueue('liu')

print([itm for itm in q.itms])
print(q.dequeue())
print([itm for itm in q.itms])


# 改进版
class Advancequeue():
    def __init__(self):
        self.itms = []

    def is_empty(self):
        return self.itms == []

    # 队头插入
    def addfront(self, itm):
        return self.itms.append(itm)

    # 队尾插入
    def enqueue1(self, itm):
        return self.itms.insert(0, itm)

    # 队尾位置删除
    def pop_rear(self):
        return self.itms.pop(0)

    # 队头位置删除
    def dequeue(self):
        return self.itms.pop()

    def size(self):
        return len(self.itms)


# 判断是否为回文字符串
def chkstr(mystr):
    flag = True
    q = Advancequeue()

    for s in mystr:
        q.addfront(s)

    while q.size() > 1 and flag:
        hstr = q.pop_rear()
        rstr = q.dequeue()
        if hstr != rstr:
            flag = False

    return flag


print(chkstr('noon'))  # True
print(chkstr('swdfewe'))  # False
