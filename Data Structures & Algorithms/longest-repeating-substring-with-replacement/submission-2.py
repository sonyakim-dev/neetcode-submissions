class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        max_count = 0
        l = 0
        result = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            max_count = max(max_count, counter[s[r]])
            while r - l - max_count + 1 > k:
                counter[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result