class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(grid), len(grid[0])
        visited = set()
        area = 0

        def dfs(r, c):
            if r not in range(row) or c not in range(col)\
                or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))
            curr = 1
            for dr, dc in direction:
                R, C = dr + r, dc + c
                curr += dfs(R, C)
            return curr

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, dfs(r, c))

        return area