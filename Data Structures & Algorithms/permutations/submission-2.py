class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        ## DFS
        # def dfs(cand, fixed):
        #     if not cand:
        #         result.append(fixed)
        #         return
        #     for i in range(len(cand)):
        #         dfs(cand[:i] + cand[i+1:], fixed + [cand[i]])

        # dfs(nums, [])
        # return result

        ## BT; start from empty list, add an el in every position on each iteration
        ## T.C: O(n! * n^2), S.C: O(n! * n)
        # if len(nums) == 1: return []

        # perms = self.permute(nums[1:])
        # for p in perms:
        #     for i in range(len(p) + 1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         result.append(p_copy)

        # return result

        # BT iter
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms