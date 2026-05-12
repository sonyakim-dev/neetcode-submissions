class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)

        if len(s) != len(t): return False

        counter1, counter2 = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            counter1[s[i]] += 1
            counter2[t[i]] += 1
        
        return counter1 == counter2

        # T.C: O(n), S.C: O(1)