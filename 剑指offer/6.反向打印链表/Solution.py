# 题目描述：
# 输入一个链表表头节点，从尾到头反过来打印每个节点到值
# 思路：
# 1.运用list中到insert方法进行插入；
# 2.运用栈的先进后出的特性；


# 方法1：list中的Insert
class Node:
    def __init__(self, x=None):
        self.data = x
        self.next = None


class Solution:
    def printReversingList(self, listNode):
        if listNode.data == None:
            return

        l = []
        head = listNode
        while head:
            l.insert(0, head.data)
            head = head.next
        return l


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

node4 = Node(4)
node5 = Node()
s = Solution()

print(s.printReversingList(node1))
print(s.printReversingList(node4))
print(s.printReversingList(node5))


# 方法二：栈
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        return self.items.append(data)

    def pop(self):
        return self.items.pop()


class Solution1:
    def printReversingList(self, headNode):
        if headNode.data == None:
            return
        stack = Stack()
        l = []
        head = headNode
        while head:
            stack.push(head.data)
            head = head.next

        while not stack.is_empty():
            l.append(stack.pop())
        return l


s1 = Solution1()
print(s1.printReversingList(node1))

print(s1.printReversingList(node4))
print(s1.printReversingList(node5))

