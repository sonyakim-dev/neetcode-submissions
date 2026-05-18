class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(cand, fixed):
            if not cand and fixed:
                result.append(fixed)
            for i in range(len(cand)):
                sub = cand[:i+1]
                if sub == sub[::-1]:
                    dfs(cand[i+1:], fixed + [sub])

        dfs(s, [])
        return result