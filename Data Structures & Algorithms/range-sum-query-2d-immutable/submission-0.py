class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.row_sum = [[] for _ in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.row_sum[r].append((0 if c == 0 else self.row_sum[r][c-1]) + matrix[r][c])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for r in range(row1, row2+1):
            result += self.row_sum[r][col2] - (self.row_sum[r][col1-1] if col1 > 0 else 0)
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)