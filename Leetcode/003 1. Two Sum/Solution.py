# -*- coding:utf-8 -*-

# 题目: 1. Two Sum
# 题目链接：https://leetcode.com/problems/two-sum/
# 题目大意：
# 给出一个整型数组，找出两个数字之和为给定target值对应的下标index，如下：
# 条件：
# 给出的的target只有两个唯一的数字之和
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# 题目解析：
# 1.找个两个值的之和等于某个值，需要遍历数组
# 2.使用反向思维，先把target减去第一个元素差放在hash表，再判断剩下的元素是否与hash表中的值相等

# 核心思想：使用hash表，使用键值对进行存储数组值(key)和下标值(value)
# 时间复杂度为o(n)

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 0: return False

        map = {}

        for i in range(0, len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return [map[nums[i]], i]

s = Solution()
print(s.twoSum([1, 3, 0, 4, 9], 5))


