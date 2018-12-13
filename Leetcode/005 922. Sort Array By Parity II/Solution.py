# -*- coding:utf-8 -*-

# Sort Array By Parity II
# 题目大意：
# 给出一个非负整数的数组A，一半是奇数，一半是偶数，返回数组的元素如果为奇数，它的下标也是奇数，如果是偶数，它是下标也是偶数
# 例如：Input: [4,2,5,7]
#      Output: [4,5,2,7]
#      Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# 题目解析：
# 这个题目是由905. Sort Array By Parity延伸过来的，与前者不同的是，返回的数据是奇偶相间的方式排序的
# 所以思路就是先把奇偶元素分为两部分，然后按照奇偶下标进行排列，排列的方式：1.直接判断下标为奇偶；2.切片思想；

# 方法1：通过判断下标为奇偶性来排序


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        output = [None] * len(A)

        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        return [even.pop() if i % 2 == 0 else odd.pop() for i in range(len(A))]
    # 时间复杂度：O(N)
    # 空间复杂度：O(N)


# 方法2：切片的思想


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        output = [None] * len(A)

        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        output[::2] = even
        output[1::2] = odd

        return output
    # 时间复杂度：O(N)
    # 空间复杂度：O(N)
