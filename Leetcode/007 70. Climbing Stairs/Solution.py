class Solution:
    def climbStairs(self, n):
        self.memo = [0 for _ in range(n + 1)]
        print(self.dp(n))

    def dp(self, n):
        self.sum = 0
        if self.memo[n] != 0:
            self.sum = self.memo[n]
        elif n <= 0:
            if n == 0:
                self.sum = 1
            else:
                self.sum = 0
        elif n > 0:
            self.sum = self.dp(n-2) + self.dp(n-1)

        self.memo[n] = self.sum
        return self.sum

