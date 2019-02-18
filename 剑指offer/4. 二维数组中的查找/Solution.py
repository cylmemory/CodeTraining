# 题目描述
# 给定一个二维数组，其每一行从左到右递增排序，从上到下也是递增排序。给定一个数，判断这个数是否在该二维数组中。
# 要求时间复杂度 O(M + N)，空间复杂度 O(1)。
# Consider the following matrix:
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
# Given target = 5, return true.
# Given target = 20, return false.
# 解题思路：
# 首先从左到右，从上到下递增的特点，可以确定从右上角上的元素开始搜索，如果大的话，往下搜索，如果小的话，往左搜索

class Solution:
    def find(self, arrs, num):
        if arrs == []:
            return False
        row_len = len(arrs)
        col_len = len(arrs[0])
        i, j = 0, col_len-1

        # 判断输入值的合法性
        if isinstance(num, float) and isinstance(arrs[0][0], int):
            if int(num) != num:
                return False
            num = int(num)
        elif isinstance(num, int) and isinstance(arrs[0][0], float):
            num = float(num)
        elif type(num) != type(arrs[0][0]):
            return False

        while i <= row_len-1 and j >= 0:
            if num == arrs[i][j]:
                return True
            elif num > arrs[i][j]:
                i += 1
            elif num < arrs[i][j]:
                j -= 1
        return False


array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
array2 = []
array3 = [['a', 'b', 'c'],
          ['b', 'c', 'd']]
array4 = [[62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],
          [63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],
          [64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],
          [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],
          [66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],
          [67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85]]

s = Solution()
print(s.find(array, 10)) # True
print(s.find(array, 30)) # False
print(s.find(array, 15.0)) # False
print(s.find(array, '')) # False
print(s.find(array2, 10)) # False
print(s.find(array3, 'b')) # True
print(s.find(array4, 81)) # True