class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    R, C = dr + r, dc + c
                    if R in range(row) and C in range(col) and grid[R][C] == 1:
                        q.append((R, C))
                        grid[R][C] = 2
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1