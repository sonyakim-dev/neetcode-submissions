class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        ## BT
        def dfs(i, fixed, target):
            if target == 0:
                result.append(fixed.copy())
                return
            if i >= len(nums) or target < 0:
                return

            dfs(i, fixed + [nums[i]], target - nums[i])
            dfs(i+1, fixed, target)

        dfs(0, [], target)
        return result


        ## DFS
        # def dfs(cand, fixed, target):
        #     if target == 0:
        #         result.append(fixed)
        #         return
        #     for i, c in enumerate(cand):
        #         if target - c >= 0:
        #             dfs(cand[i:], fixed + [c], target - c)
            
        # dfs(nums, [], target)
        # return result