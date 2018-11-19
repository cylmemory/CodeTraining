# -*- coding:utf-8 -*-

# 题目: 941. Valid Mountain Array
# 题目链接：https://leetcode.com/problems/valid-mountain-array/
# 题目大意：
# 给出一个数组，判断是否为山峰数组，如下：
# 条件：
# 1.数组A长度要大于等于3
# 2.存在0<i<A.length-1,使得：
#   A[0] < A[1] < ... A[i-1] < A[i]
#   A[i] > A[i+1] > ... > A[A.length - 1]
#
# Example 1:
#
# Input: [2,1]
# Output: false
# Example 2:
#
# Input: [3,5,5]
# Output: false
# Example 3:
#
# Input: [0,3,2,1]
# Output: true

# 题目解析：
# 给出一个数组是否为山峰数组（两边低，中间高），需要分别在数组头尾两边向中间进行检索出最大值
# 最终判断这两个最大值是否相等
# 时间复杂度为o(n)


class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3: return False

        start, end, length = 0, len(A) - 1, len(A)

        while start + 1 < length and A[start] < A[start + 1]:
            start += 1
        while end > 0 and A[end] < A[end - 1]:
            end -= 1

        return 0 < start == end < length - 1