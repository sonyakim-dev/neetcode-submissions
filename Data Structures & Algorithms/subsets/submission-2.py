class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ## dp; either include itself or not
        # result = []
        # subset = []

        # def dfs(i):
        #     if i >= len(nums):
        #         result.append(subset.copy())
        #         return
        #     subset.append(nums[i])
        #     dfs(i + 1)
        #     subset.pop()
        #     dfs(i + 1)

        # dfs(0)
        # return result

        result = [[]]
        for n in nums:
            result += [el + [n] for el in result]
        return result