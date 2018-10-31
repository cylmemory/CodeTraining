# -*- coding: utf-8 -*-
class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # 压栈
    def push(self, item):
        self.items.append(item)

    #  弹栈
    def pop(self):
        return self.items.pop()

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items)-1]

    # 返回栈的大小
    def size(self):
        return len(self.items)


# test
s = Stack()
print(s.is_empty())  # True

s.push(3)  # s = [3]
s.push('cat')  # s = ['cat', 3]

print(s.is_empty())  # False
print(s.size())  # 2
print(s.peek())  # 'cat'

print(s.pop())  # 'cat'
print(s.size())  # '1'
print(s.peek())  # 3
