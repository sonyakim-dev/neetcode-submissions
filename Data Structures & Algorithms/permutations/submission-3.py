class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        unique el
        """
        result = []
        def dfs(cand, fixed):
            # base case
            if not cand:
                result.append(fixed)
                return
                
            for i in range(len(cand)):
                dfs(cand[:i] + cand[i+1:], fixed + [cand[i]])

        dfs(nums, [])
        return result