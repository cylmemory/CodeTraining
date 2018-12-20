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