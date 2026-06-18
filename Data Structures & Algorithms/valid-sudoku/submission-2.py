class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, square = set(), set(), set() # (index, value)
        # square index: (rows // 3, cols // 3)
        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == '.': continue
                if (r, val) in rows: return False
                if (c, val) in cols: return False
                if ((r//3, c//3), val) in square: return False

                rows.add((r, val))
                cols.add((c, val))
                square.add(((r//3, c//3), val))
        return True
