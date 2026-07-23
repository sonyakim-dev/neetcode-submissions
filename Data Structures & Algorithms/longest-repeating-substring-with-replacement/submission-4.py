class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        longest = 1
        max_count = 0
        l = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            if counter[s[r]] > max_count:
                max_count = counter[s[r]]
            
            while r - l + 1 - max_count - k > 0:
                counter[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            
        return longest