# 题目：Climbing Stairs
#
# 题目链接：https://leetcode.com/problems/climbing-stairs/
# 题目大意：
# 给出一个n阶的楼梯，每次只能爬1阶或者2阶，求出总共需要多少中爬法
# 条件：
# n为正整数
#
# example1
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
# example2
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# 题目解析：
# 1.将大问题分解为小问题：求n个阶梯走法dp[n]，可以分解为dp[n]=dp[n-1]+dp[n-2]
# 2.注意分界点:方法1：n<=0 和方法2：dp[0]=1 dp[1]=2
# 3.备忘录
# 核心思想：动态规划

# 方法1：自上而下
class Solution:
    def climbStairs(self, n):
        self.memo = [0 for i in range(n + 1)]

        print(self.dp(n))

    def dp(self, n):
        self.m = 0
        if self.memo[n] != 0:
            self.m = self.memo[n]
        elif n <= 0:
            if n == 0:
                self.m = 1
            else:
                self.m = 0
        elif n > 0:
            self.m = self.dp(n - 2) + self.dp(n - 1)

        self.memo[n] = self.m
        return self.m

# 方法2：基于斐波拉契数列（Fibonacci）
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        memo = [0 for _ in range(n)]
        memo[0], memo[1] = 1, 2

        return self.dp(n-1, memo)

    def dp(self, n, memo):
        if memo[n] == 0:
            memo[n] = self.dp(n-1, memo) + self.dp(n-2, memo)
        return memo[n]
