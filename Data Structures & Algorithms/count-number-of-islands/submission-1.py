class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        count = 0

        def dfs(r, c):
            if r not in range(row) or c not in range(col)\
                or (r, c) in visited or grid[r][c] == "0":
                return False
            visited.add((r, c))
            for dr, dc in direction:
                R, C = dr + r, dc + c
                dfs(R, C)
            return True

        for r in range(row):
            for c in range(col):
                if dfs(r, c): count += 1

        return count