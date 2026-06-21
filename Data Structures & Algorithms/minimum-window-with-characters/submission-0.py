class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ''
        
        count_s, count_t = defaultdict(int), Counter(t)
        have, need = 0, len(t)
        l = 0
        result = None

        for r in range(len(s)):
            c = s[r]
            count_s[c] += 1

            # record current char count
            if c in count_t and count_s[c] <= count_t[c]:
                have += 1
            
            # check need and have: if have < need, keep moving r
            # else, keep moving l to find minimum substr
            while have >= need:
                if not result or r - l + 1 < len(result):
                    result = s[l:r+1]
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        return result if result != None else ''
