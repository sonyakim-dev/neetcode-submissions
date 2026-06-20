class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        size1, size2 = len(word1), len(word2)
        result = ''

        while i < size1 or j < size2:
            if i == size1:
                return result + word2[j:]
            if j == size2:
                return result + word1[i:]
            
            result += word1[i] + word2[j]
            i += 1
            j += 1

        return result