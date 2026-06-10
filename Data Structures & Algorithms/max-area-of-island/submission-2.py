class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        area = 0

        def dfs(r, c):
            if not 0 <= r < row or not 0 <= c < col or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            count = 1
            for dr, dc in direction:
                count += dfs(r + dr, c + dc)
            return count

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, dfs(r, c))
        return area
                    