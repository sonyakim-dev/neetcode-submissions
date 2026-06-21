class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep the most common char, replace others
        counter = defaultdict(int)
        max_count = 0
        longest = 0
        l = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            max_count = max(max_count, counter[s[r]])
            while r - l + 1 - max_count - k > 0:
                counter[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest