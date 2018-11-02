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


# 利用栈来反转字符串
# 思路：先取每个字符压栈，再弹栈
def reverse(mystr):
    output_str = ''
    mystack = Stack()

    if(len(mystr) == 0):
        return ''
    for s in mystr:
        mystack.push(s)

    while not mystack.is_empty():
        output_str += mystack.pop()

    return output_str


print(reverse(''))
print(reverse('123456789'))
print(reverse('abc'))
print(reverse('12321'))


# 判断括号匹配
# 思路：先检索是否为左边方向的括号，然后压栈，当检索为右边方向的括号，再把栈顶元素(最近位置)弹栈来进行匹配
def match(lStr, rStr):
    leftStrings = '{[('
    rightstrings = '}])'

    return leftStrings.index(lStr) == rightstrings.index(rStr)


def checksymbolbalance(symbolstring):
    s = Stack()
    index = 0
    flag = True
    while index < len(symbolstring) and flag:
        if symbolstring[index] in '{[(':
            s.push(symbolstring[index])
        else:
            if s.is_empty():
                return False
            else:
                lstr = s.pop()
                if not match(lstr, symbolstring[index]):
                    flag = False
        index += 1
    if flag and s.is_empty():
        return True
    else:
        return False


print(checksymbolbalance('{([]((){}))}'))


# 十进制数转化成各个进制
# base--几进制
def convertto(decnumber, base):
    s = Stack()
    digis = '0123456789ABCDEF'
    output = ''

    while decnumber > 0:
        result = decnumber % base
        s.push(result)

        decnumber = decnumber // base
    while not s.is_empty():
        output += digis[s.pop()]

    return output


print(convertto(59, 8))


# 十进制转换为二进制
# 思路：先把这个值除于2取模，压栈，再弹栈
def DecToBin(decnumber):
    s = Stack()
    output = ''

    while decnumber > 0:
        result = decnumber % 2
        s.push(result)

        decnumber = decnumber // 2
    while not s.is_empty():
        output += str(s.pop())

    return output


print(DecToBin(42))


def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())

    return ''.join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))