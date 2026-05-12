class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        record = defaultdict(lambda: 0)
        for i in range(len(s)):
            record[s[i]] += 1
            record[t[i]] -= 1
        
        for r in record.values():
            if r != 0: return False
        return True