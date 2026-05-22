class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for s in strs:
            if not s.startswith(result):
                while result and not s.startswith(result):
                    result = result[:-1]

        return result