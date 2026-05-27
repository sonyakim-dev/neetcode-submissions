class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(grid), len(grid[0])
        count, time = 0, 0
        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    count += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        while q and count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    R, C = dr + r, dc + c
                    if 0 <= R < row and 0 <= C < col and grid[R][C] == 1:
                        q.append((R, C))
                        grid[R][C] = 2 # update banana
                        count -= 1
            time += 1

        return time if count == 0 else -1