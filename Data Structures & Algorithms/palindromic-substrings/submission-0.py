class Solution:
    def countSubstrings(self, s: str) -> int:
        result = []
        size = len(s)

        for i in range(size):
            l, r = i, i
            while l >= 0 and r < size and s[l] == s[r]:
                result.append(s[l:r+1])
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < size and s[l] == s[r]:
                result.append(s[l:r+1])
                l -= 1
                r += 1
        
        return len(result)