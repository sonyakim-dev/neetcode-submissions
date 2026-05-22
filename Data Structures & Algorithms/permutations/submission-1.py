class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(cand, fixed):
            if not cand:
                result.append(fixed)
                return
            for i in range(len(cand)):
                dfs(cand[:i] + cand[i+1:], fixed + [cand[i]])

        dfs(nums, [])
        return result