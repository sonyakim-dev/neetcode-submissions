class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # do not go up or left, either down or right!

        ## DFS
        # def dfs(r, c):
        #     if r == (m - 1) and c == (n - 1):
        #         return 1
        #     if r >= m or c >= n:
        #         return 0

        #     return dfs(r + 1, c) + dfs(r, c + 1)

        # return dfs(0, 0)


        ## DP
        row = [1] * n

        for i in range(m - 1):
            for j in range(1, n):
                row[j] += row[j-1]
        return row[-1]
