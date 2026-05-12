class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, square = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".": continue
                if val in row[i] or val in col[j] or val in square[(i//3, j//3)]:
                    return False
                row[i].add(val)
                col[j].add(val)
                square[(i//3, j//3)].add(val)
        
        return True
