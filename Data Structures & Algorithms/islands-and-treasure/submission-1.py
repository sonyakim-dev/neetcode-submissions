class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(grid), len(grid[0])
        INF = 2147483647
        q = deque() # (row, col, distance)
        visited = set()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
            
        while q:
            for i in range(len(q)):
                r, c, d = q.popleft()
                grid[r][c] = min(grid[r][c], d)
                visited.add((r, c))
                for dr, dc in direction:
                    R, C = dr + r, dc + c
                    if 0 <= R < row and 0 <= C < col\
                        and (R, C) not in visited and grid[R][C] != -1:
                        q.append((R, C, d + 1))
            