class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for r in range(len(matrix)):
            for c in range(1, len(matrix[0])):
                self.matrix[r][c] += self.matrix[r][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for r in range(row1, row2 + 1):
            result += self.matrix[r][col2] - (self.matrix[r][col1-1] if col1 > 0 else 0)
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)