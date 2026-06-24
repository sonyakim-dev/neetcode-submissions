class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word) - 1:
                return True

            visited.add((r, c))
            for dr, dc in direction:
                R, C = dr + r, dc + c
                if 0 <= R < row and 0 <= C < col\
                    and (R, C) not in visited and board[R][C] == word[i+1]:
                    if dfs(R, C, i + 1): return True
            visited.remove((r, c))

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0): return True
        return False