# -*- coding:utf-8 -*-

# X of a Kind in a Deck of Cards
# 题目大意：
# 一副写着整数的牌,当返回True时，即可以把这副牌分为1组或者多组，没每组的牌数量X>=2：
# 1.每组牌数量为X
# 2.每组牌的数量都相同

# 例1：
# 输入：[1,2,3,4,4,3,2,1]
# 输出：true
#  说明：可能的分区[1,1]，[2,2]，[3,3]，[4,4]

# 例2：
# 输入：[1,1,1,2,2,2,3,3]
# 输出：false
#  说明：没有可能的分区。

# 例3：
# 输入：[1]
# 输出：false
#  说明：没有可能的分区。

# 例4：
# 输入：[1,1]
# 输出：true
#  说明：可能的分区[1,1]

# 例5：
# 输入：[1,1,2,2,2,2]
# 输出：true
#  说明：可能的分区[1,1]，[2,2]，[2,2]
#
# 题目解析：
# 一开始觉得有点难理解，题目主要是讲，给出一个数组，是否能分为1-n组，每一组的数据必须相同，且每一组数据有X个，X>=2
# 首先第一步，先统计给出的数组的元素重复数量，运用collections模块的Counter类来统计
# 接着，求出其中的最大公约数，如果大于1，则为True，反之False


class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from functools import reduce
        import collections
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = collections.Counter(deck).values()
        return reduce(gcd, count) > 1

