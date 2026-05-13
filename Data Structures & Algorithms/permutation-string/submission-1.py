class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)

        for i in range(0, len(s2) - len(s1) + 1):
            if Counter(s2[i:i + len(s1)]) == count1:
                return True

        return False