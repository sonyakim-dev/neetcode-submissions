class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        area = 0

        def dfs(r, c):
            if not 0 <= r < row or not 0 <= c < col or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        return area
