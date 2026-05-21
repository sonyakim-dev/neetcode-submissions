class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        memo = { size: 1 }

        def dfs(i):
            if i in memo: return memo[i]
            if s[i] == "0": return 0

            result = dfs(i+1)
            if i < size - 1 and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                result += dfs(i+2)
            memo[i] = result
            return result

        return dfs(0)