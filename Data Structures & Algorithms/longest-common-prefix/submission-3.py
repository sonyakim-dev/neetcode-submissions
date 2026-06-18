class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # result = strs[0]

        # for s in strs:
        #     if not s.startswith(result):
        #         while result and not s.startswith(result):
        #             result = result[:-1]

        # return result
        # T.C: O(n * m), S.C: O(m)

        strs.sort()
        str1, str2 = strs[0], strs[-1]
        i = 0
        while i < len(str1) and str1[i] == str2[i]:
            i += 1
        return str1[:i]