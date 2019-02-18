# 题目描述
# 在一个长度为 n 的数组里的所有数字都在 0 到 n-1 的范围内。
# 数组中某些数字是重复的，但不知道有几个数字是重复的，也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
# 要求是时间复杂度 O(N)，空间复杂度 O(1)
# example:
# Input:
# {2, 3, 1, 0, 2, 5}
#
# Output:
# 2

# 思路：
# 首先，根据时间复杂度和空间复杂度的要求，不能使用排序方法。
# 可以根据数组[0,n-1]中，将值为i的元素调整到第i个位置来进行判读啊是否重复


class Solution:

    def duplicate(self, numbers, duplication):

        if numbers == None or len(numbers) <= 0:
            return False

        for i in numbers:
            if i < 0 or i > len(numbers)-1:
                return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    index = numbers[i]
                    numbers[i], numbers[index] = numbers[index], numbers[i]
        return False


test = [2, 3, 1, 0, 2, 5, 3]
s = Solution()
duplication = [0]
print(s.duplicate(test, duplication))
