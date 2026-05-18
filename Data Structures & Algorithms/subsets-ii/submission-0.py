class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # for each element, make dicision to either include it or not
        result = []
        subset = []
        nums.sort()

        def dfs(cand, path):
            result.append(path)

            for i in range(len(cand)):
                if i > 0 and cand[i] == cand[i-1]: continue
                dfs(cand[i+1:], path + [cand[i]])

        dfs(nums, [])
        return result