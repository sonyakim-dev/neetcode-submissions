class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(cand, path):
            if not cand:
                result.append(path)
                return
            for i in range(len(cand)):
                dfs(cand[:i] + cand[i+1:], path + [cand[i]])
        
        dfs(nums, [])
        return result