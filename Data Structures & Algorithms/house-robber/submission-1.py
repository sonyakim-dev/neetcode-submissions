class Solution:
    def rob(self, nums: List[int]) -> int:
        # in i position, rob either i+1 or i+2
        # same as climbig stairs problem
        # keep repeating the subproblem by adding curr

        # top-down
        memo = {}

        def dfs(i):
            if i >= len(nums): return 0
            if i in memo: return memo[i]
            memo[i] = max(dfs(i+1), dfs(i+2) + nums[i])
            return memo[i]

        return dfs(0)

        # bottom-up
        # rob1, rob2 = 0, nums[0]
        # for i in range()