class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        size1, size2 = len(word1), len(word2)
        memo = [[float("inf")] * (size2 + 1) for _ in range(size1 + 1)]

        for j in range(size2 + 1):
            memo[size1][j] = size2 - j
        for i in range(size1 + 1):
            memo[i][size2] = size1 - i
        
        for i in range(size1 - 1, -1, -1):
            for j in range(size2 -1, -1, -1):
                if word1[i] == word2[j]:
                    memo[i][j] = memo[i+1][j+1]
                else:
                    memo[i][j] = 1 + min(memo[i+1][j], memo[i][j+1], memo[i+1][j+1])
        
        return memo[0][0]