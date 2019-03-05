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


# list define and operating
class LList:
    def __init__(self):
        self.head = None
        self._rear = None

    def is_empty(self):
        return self.head is None or self._rear is None

    def add(self, elem):
        tempnode = Node(elem)
        tempnode.set_next(self.head)
        self.head = tempnode
        if tempnode.next is not None:
            self._rear = tempnode.next
        else:
            self._rear = tempnode

    def remove(self, elem):
        current = self.head
        pre = None
        isFound = False

        while not isFound:
            if current.get_data() == elem:
                isFound = True
            else:
                pre = current
                current = current.get_next()

        if pre is None:
            # delete head node
            self.head = current.get_next()
        else:
            # delete other node except head node
            pre.set_next(current.get_next())

    def search(self, elem):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == elem:
                found = True
            else:
                current = current.get_next()
        return found


# double list node
class DLNode(Node):
    def __init__(self, elem, prev=None):
        Node.__init__(self, elem)
        self.prev = prev


# double list class
class DLList(LList):
    def __init__(self):
        LList.__init__(self)

    # 头部插入
    def prepend(self, elem):
        p = DLNode(elem)
        if self.head is None:
            self._rear = p
        else:
            p.next.prev = p
        self.head = p

    # 尾部插入
    def append(self, elem):
        p = DLNode(elem)
        if self.head is None:
            self.head = p
        else:
            p.prev.next = p
        self._rear = p

    # 删除首部节点
    def pop(self):
        if self.head is None:
            print('this is an empty double list')
            return
        e = self.head.data
        self.head = self.head.next
        if self.head is not None:   # 为空时不需要做任何事
            self.head.prev = None
        return e

    # 删除尾部节点
    def pop_last(self):
        if self.head is None:
            print('this is an empty double list')
            return
        e = self._rear.data
        self._rear = self._rear.prev
        if self._rear is None:  # 为空时,要把头节点设为None 不为空,则把next指针设为None
            self.head = None
        else:
            self._rear.next = None
        return e



