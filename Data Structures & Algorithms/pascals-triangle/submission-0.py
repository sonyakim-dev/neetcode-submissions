class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # DP - bottom-up
        result = [[1]]
        for n in range(numRows - 1):
            curr = []
            prev = result[-1]
            for i in range(len(prev)-1):
                curr.append(prev[i] + prev[i+1])
            result.append([1] + curr + [1])
        return result
