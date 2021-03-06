# 题目：收集苹果
#
# 题目大意：
# 平面上有N*M个格子，每个格子中放着一定数量的苹果。你从左上角的格子开始，
# 每一步只能向下走或是向右走，每次走到一个格子上就把格子里的苹果收集起来，
# 这样下去，你最多能收集到多少个苹果。
# 条件：
# n为正整数
#
#     [[5, 8, 5, 7, 1, 8],
#      [1, 3, 2, 8, 7, 9],
#      [7, 8, 6, 6, 8, 7],
#      [9, 9, 8, 1, 6, 3],
#      [2, 4,10, 2, 6, 2],
#      [5, 5, 2, 1, 8, 8]
#     ]
# 最大值是 76 (i.e., 5+8+5+7+8+7+8+6+6+8+8 = 76).
#
# 题目思路：
# 1.解这个问题与解其它的DP问题几乎没有什么两样。第一步找到问题的“状态”，第二步找到“状态转移方程”，然后基本上问题就解决了。
#
# 首先，我们要找到这个问题中的“状态”是什么？我们必须注意到的一点是，到达一个格子的方式最多只有两种：
# 从左边来的(除了第一列)和从上边来的(除了第一行)。因此为了求出到达当前格子后最多能收集到多少个苹果，
# 我们就要先去考察那些能到达当前这个格子的格子，到达它们最多能收集到多少个苹果。
# (本质其实是DP的关键：欲求问题的解，先要去求子问题的解)
#
# 经过上面的分析，很容易可以得出问题的状态和状态转移方程。状态dp[i][j]表示我们走到(i, j)这个格子时，最多能收集到多少个苹果。那么，状态转移方程如下：
# dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + arr[i][j]

# 核心思想：动态规划
# 1.确定状态表示
# 2.状态转移
# 3.初始状态和边界问题


# 方法一：

class Solution:
    def collection(self, arr):
        dp = [[0 for i in range(len(row))] for row in arr]

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if i == 0 and j == 0:
                    dp[i][j] = arr[i][j]
                if i == 0:
                    dp[i][j] = dp[i][j-1] + arr[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + arr[i][j]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + arr[i][j]
        print(dp[i][j])
        print(dp)



s = Solution()
s.collection([[5, 8, 5, 7, 1, 8], [1, 3, 2, 8, 7, 9], [7, 8, 6, 6, 8, 7], [9, 9, 8, 1, 6, 3],
              [2, 4,10, 2, 6, 2], [5, 5, 2, 1, 8, 8]])