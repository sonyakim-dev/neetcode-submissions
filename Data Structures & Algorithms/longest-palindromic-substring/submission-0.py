class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        size = len(s)

        # start from the middle letter and expand to both direction
        for i in range(size):
            # odd length
            l, r = i, i
            while l >= 0 and r < size and s[l] == s[r]:
                if (r - l + 1) > len(result):
                    result = s[l:r+1]
                l -= 1
                r += 1
            # even legnth
            l, r = i, i+1
            while l >= 0 and r < size and s[l] == s[r]:
                if (r - l + 1) > len(result):
                    result = s[l:r+1]
                l -= 1
                r += 1
        
        return result