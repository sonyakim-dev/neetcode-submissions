class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(r, c, i):
            if i == len(word): return True
            if r not in range(row) or c not in range(col)\
                or (r, c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r, c))
            for dr, dc in direction:
                if dfs(dr + r, dc + c, i + 1): return True
            visited.remove((r, c))
            return False                    
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0): return True
        return False