# -*- coding:utf-8 -*-

# 题目: 942. DI String Match
# 题目链接：https://leetcode.com/problems/di-string-match/
# 题目大意：
# 给出只包含'D'和'I'的字符串S，D代表降序，I代表升序，按照S每个字符代表的升降顺序来返回[0,1...N]符合该顺序的数据，如下：
# 条件：
# 1.1 <= S.length <= 10000
# 2.S只包含D和I的任意字符串
#
# Example 1:

# Input: "IDID"
# Output: [0,4,1,3,2]
# Example 2:

# Input: "III"
# Output: [0,1,2,3]
# Example 3:

# Input: "DDI"
# Output: [3,2,0,1]

# 题目解析：
# 按照指定顺序返回数组，必须考虑：
# 1.确定数组长度为字符串S的长度加1
# 2.建立一个空数组res
# 2.两个数字之间的有效排序：
#     a.升序，取最大数字的元素依次插入res数组中
#     b.降序，取最小数字的元素依次插入res数组中
#     c.剩下的直接插入尾部

# 核心思想：当为"D"，把最大数据插入数组，为"I"，把最小数据插入数组
# 时间复杂度为o(n)

class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ls = list(range(len(S) + 1))

        res = []

        for i in S:
            if i == 'D':
                res.append(ls.pop())
            else:
                res.append(ls.pop(0))

        return res + ls


class Solution1:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l, r, res = 0, len(S), []

        for i in S:
            if i == "D":
                res.append(r)
                r -= 1
            else:
                res.append(l)
                l += 1
        return res + [l]