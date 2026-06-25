class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        subs = []

        def dfs(i):
            if i == len(s):
                result.append(subs.copy())
                return

            for j in range(i, len(s)):
                st = s[i:j+1]
                if st == st[::-1]:
                    subs.append(st)
                    dfs(j+1)
                    subs.pop()

        dfs(0)
        return result