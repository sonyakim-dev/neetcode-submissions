class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # think 2d array as an 1d array since it is strictly ascending order
        row, col = len(matrix), len(matrix[0]) # 3, 4
        l, r = 0, row * col - 1 # 0, 11
        while l <= r:
            m = (l + r) // 2 # 5
            if matrix[m // col][m % col] > target:
                r = m - 1
            elif matrix[m // col][m % col] < target:
                l = m + 1
            else:
                return True
        return False