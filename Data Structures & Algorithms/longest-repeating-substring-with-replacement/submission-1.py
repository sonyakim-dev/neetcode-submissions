class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep the most common char, and replace other chars
        counter = defaultdict(int)
        result, l, freq = 0, 0, 0

        for r in range(len(s)):
            counter[s[r]] += 1
            freq = max(freq, counter[s[r]])
            while r - l + 1 - freq > k:
                counter[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)

        return result