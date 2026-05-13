class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix) - 1
        col_l, col_r = 0, len(matrix[0]) - 1

        while row_l <= row_r:
            row_m = (row_l + row_r) // 2
            r1, r2 = matrix[row_m][0], matrix[row_m][-1]
            if r1 <= target <= r2:
                while col_l <= col_r:
                    col_m = (col_l + col_r) // 2
                    if target == matrix[row_m][col_m]:
                        return True
                    elif target > matrix[row_m][col_m]:
                        col_l = col_m + 1
                    else:
                        col_r = col_m - 1
                return False
            elif target > r2:
                row_l = row_m + 1
            else:
                row_r = row_m - 1

    
        return False