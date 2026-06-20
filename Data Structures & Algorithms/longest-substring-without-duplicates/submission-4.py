class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] in record:
                while l < r and s[l] != s[r]:
                    record.remove(s[l])
                    l += 1
                l += 1
            else:
                longest = max(longest, r - l + 1)
                record.add(s[r])
                
        return longest

