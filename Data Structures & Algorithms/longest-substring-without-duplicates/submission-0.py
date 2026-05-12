class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = set()
        count, l = 0, 0

        for r in range(len(s)):
            while s[r] in record:
                record.remove(s[l])
                l += 1
            record.add(s[r])
            count = max(count, r-l + 1)
        return count