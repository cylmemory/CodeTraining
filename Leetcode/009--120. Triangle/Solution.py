# 题目：120. Triangle
#
# 题目链接：https://leetcode.com/problems/triangle/
# 题目大意：
# 给出一个三角数塔，从顶层到底层，每步只能走下一层相连到到节点，求出走过到节点之和最小值
# 条件：
# n为正整数
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# 题目解析：
# 1.从顶部到底部，如果要到来第i层，就必须先到i-1层，如果是到达第i层的第j个元素，那只能是i-1层的第j和j-1个元素才能到达第i层的第j个元素，这个可能
#   比较难理解。
# 2.其次，要到每一层的首尾元素，就只能是上一层的对应的首尾元素到达，增加边缘元素的判断，这点也比较关键
# 3.当走到第i层第j个元素时，求最小值res[i][j]=min(res[i-1][j], res[i-1][j-1]) + triangle[i][j]，即：走到哪那个元素时，求在上层中最小值加上
#   这个元素的值。
# 4.注意分界点初始值为塔顶元素res[0][0]=triangle[0][0]
# 5.最后筛选出最后一组元素中的最小值
# 核心思想：动态规划

# 方法一：


class Solution:
    def minimumTotal(self, triangle):
        self.res = [[0 for i in range(len(row))] for row in triangle]
        self.res[0][0] = triangle[0][0]
        return self.dp(triangle)

    def dp(self, triangle):
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    self.res[i][j] = self.res[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    self.res[i][j] = self.res[i - 1][j - 1] + triangle[i][j]
                else:
                    self.res[i][j] = min(self.res[i - 1][j], self.res[i - 1][j - 1]) + triangle[i][j]
        return min(self.res[-1])


s = Solution()
s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])

# 方法二：与方法一中设定和传递值一样二维数组保存最小值不同，这个方法只设定len(triangle)+1大小一维数组，求每一个元素的最小值
# dp[i]=row[i] + min(dp[i], dp[i + 1]),另外是从底部到顶部的方式，方法一是从顶部到底部

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [0 for i in range(len(triangle) + 1)]

        for row in triangle[::-1]:
            for i in range(len(row)):
                dp[i] = row[i] + min(dp[i], dp[i + 1])

        return dp[0]