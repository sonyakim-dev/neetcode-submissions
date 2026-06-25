class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    new_perms.append(p[:i] + [n] + p[i:])
            perms = new_perms
        return perms
