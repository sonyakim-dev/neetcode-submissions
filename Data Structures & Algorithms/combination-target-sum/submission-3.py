class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(cand, path, target):
            if target == 0:
                result.append(path)
                return
            for i, c in enumerate(cand):
                if target - c >= 0:
                    dfs(cand[i:], path + [c], target - c)
            
        dfs(nums, [], target)
        return result