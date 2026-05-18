class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # breath first search
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(grid), len(grid[0])
        INF = 2 ** 31 - 1
        q = deque()
        visited = set()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        while q:
            for i in range(len(q)):
                r, c, d = q.popleft()
                if r not in range(row) or c not in range(col)\
                    or (r, c) in visited or grid[r][c] == -1:
                    continue
                visited.add((r, c))
                grid[r][c] = d
                for dr, dc in direction:
                    q.append((dr + r, dc + c, d + 1))
