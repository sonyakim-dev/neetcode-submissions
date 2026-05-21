class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        size = len(s)

        for i in range(size):
            # odd length
            l, r = i, i
            while l >= 0 and r < size:
                if s[l] != s[r]: break
                if r - l + 1 > len(result):
                    result = s[l:r+1]
                l -= 1
                r += 1

            # even length
            l, r = i, i+1
            while l >= 0 and r < size:
                if r >= size: break
                if s[l] != s[r]: break
                if r - l + 1 > len(result):
                    result = s[l:r+1]
                l -= 1
                r += 1
        return result