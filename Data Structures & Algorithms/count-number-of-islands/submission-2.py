class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        count = 0

        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in direction:
                R, C = dr + r, dc + c
                if R in range(row) and C in range(col) and (R, C) not in visited and grid[R][C] == "1":
                    dfs(R, C)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    count += 1
        return count