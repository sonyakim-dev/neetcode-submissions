class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort() # [1,2,2,4,5,6,9]

        def dfs(cand, path, total):
            if total == target:
                result.append(path.copy())
                return
            for i in range(len(cand)):
                if i > 0 and cand[i] == cand[i-1]: continue
                if cand[i] + total <= target:
                    dfs(cand[i+1:], path + [cand[i]], total + cand[i])

        dfs(candidates, [], 0)
        return result