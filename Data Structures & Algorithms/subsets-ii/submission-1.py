class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        contain dups, all possible subset, not dup subsets
        BT problem; on each step decide to include the current val or not
        """
        result =  []
        nums.sort() # [1,1,2]

        ## DFS
        # def dfs(cand, path):
        #     result.append(path)

        #     for i in range(len(cand)):
        #         if i > 0 and cand[i] == cand[i-1]: continue
        #         dfs(cand[i+1:], path + [cand[i]])

        # dfs(nums, [])
        # return result


        ## DFS - efficient space
        def dfs(i, fixed):
            result.append(fixed)

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                dfs(j + 1, fixed + [nums[j]])

        dfs(0, [])
        return result