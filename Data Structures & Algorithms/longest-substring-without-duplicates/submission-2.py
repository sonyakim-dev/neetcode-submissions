class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in record:
                record.remove(s[l])
                l += 1
            record.add(s[r])
            result = max(result, r - l +1)

        return result