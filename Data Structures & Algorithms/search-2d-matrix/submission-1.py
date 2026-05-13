class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # treat matrix as a one long list since its sorted
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col - 1

        while l <= r:
            m = (l + r) //2
            i, j = m // col, m % col
            if target > matrix[i][j]:
                l = m + 1
            elif target < matrix[i][j]:
                r = m - 1
            else:
                return True
        return False