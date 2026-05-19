class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # if any of "O" touches the edge, it is not surrounded by "X"
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(board), len(board[0])
        visited = set()
        
        def dfs(r, c, mark=False):
            if (r, c) in visited: return
            if mark: board[r][c] = "X"

            visited.add((r, c))
            for dr, dc in direction:
                R, C = dr + r, dc + c
                if R in range(row) and C in range(col) and board[R][C] == "O":
                    dfs(R, C, mark)
        
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
                    dfs(r, c, True)
        
