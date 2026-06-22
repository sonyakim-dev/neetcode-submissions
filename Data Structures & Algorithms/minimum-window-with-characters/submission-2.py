class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''

        result = None
        count_s, count_t = defaultdict(int), Counter(t)
        need, have = len(t), 0
        l = 0

        for r in range(len(s)):
            c = s[r]
            count_s[c] += 1
            if c in count_t and count_s[c] <= count_t[c]:
                have += 1
            
            while have >= need:
                if not result or len(result) > r - l + 1:
                    result = s[l:r + 1]
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        return result if result != None else ''