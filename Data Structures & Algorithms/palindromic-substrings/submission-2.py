class Solution:
    def countSubstrings(self, s: str) -> int:
        # two pointers
        size = len(s)
        result = 0

        for i in range(size):
            l, r = i, i
            while l >= 0 and r < size and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < size and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1

        return result