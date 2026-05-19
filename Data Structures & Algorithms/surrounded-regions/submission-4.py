class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # if any of "O" touches the edge, it is not surrounded by "X"
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(board), len(board[0])
        
        def dfs(r, c):
            if r not in range(row) or c not in range(col) or board[r][c] != "O":
                return
            board[r][c] = "T"
            for dr, dc in direction:
                R, C = dr + r, dc + c
                dfs(R, C)
        
        # find "O"s on edges and add in visited
        for r in range(row):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][col-1] == "O":
                dfs(r, col-1)
        for c in range(col):
            if board[0][c] == "O":
                dfs(0, c)
            if board[row-1][c] == "O":
                dfs(row-1, c)
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        
