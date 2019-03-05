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


# temp = Node(93)
# temp.set_data(66)
# print(temp.data)


# list define and operating
class LList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, elem):
        tempnode = Node(elem)
        tempnode.set_next(self.head)
        self.head = tempnode

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


mylist = LList()
mylist.add(11)
mylist.add(22)
mylist.add(33)
mylist.add(44)
mylist.add(55)
print(mylist.search(44))
mylist.remove(33)
print(mylist.search(33))



