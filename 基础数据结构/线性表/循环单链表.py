# -*- coding: utf-8 -*-


# list node class
class Node:
    def __init__(self, initData):
        self.data = initData
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, nextNode):
        self.next = nextNode


class CycleList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    # 前端插入
    def prepend(self, elem):
        p = Node(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    # 后端插入
    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    # 前端弹出
    def delete_start(self):
        if self._rear is None:
            print('this is an empty cycle list')
            return
        p = self._rear.next

        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.data

    # 后端弹出
    def delete_rear(self):
        if self._rear is None:
            print('this is an empty cycle list')
            return
        p = self._rear.next

        if self._rear is p:
            self._rear = None
            return p.data

        while p.next is not self._rear:
            p = p.next
        else:
            p.next = self._rear.next
            self._rear = p

        return p.data

    # 循环单链表值打印
    def print_cycle_list_value(self):
        list = []
        if self.is_empty():
            return []

        p = self._rear.next

        while True:
            list.append(p.data)
            if p is self._rear:
                break
            p = p.next

        print([list[i] for i in range(0, len(list))])


list1 = CycleList()
list1.append('node1')
list1.append('node2')
list1.append('node3')
list1.append('node4')
list1.print_cycle_list_value()  # ['node1', 'node2', 'node3', 'node4']
print(list1._rear.data)  # rear: node4

print(list1.delete_start())  # delete node1
list1.print_cycle_list_value()   # ['node2', 'node3', 'node4']
print(list1._rear.data)  # rear: node4

list1.delete_rear()  # delete node4
list1.print_cycle_list_value()  # ['node2', 'node3']
print(list1._rear.data)  # rear: node3







