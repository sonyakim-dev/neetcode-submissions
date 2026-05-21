class Solution:
    def numDecodings(self, s: str) -> int:
        ## Top-down DP
        # size = len(s)
        # memo = { size: 1 }

        # def dfs(i):
        #     if i in memo: return memo[i]
        #     if s[i] == "0": return 0

        #     result = dfs(i+1)
        #     if i < size - 1 and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
        #         result += dfs(i+2)
        #     memo[i] = result
        #     return result

        # return dfs(0)


        ## Bottom-up DP
        curr = 0
        one, two = 1, 0 # one is a base case for len(s)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = one

            if i < len(s) - 1 \
                and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                curr += two
            curr, one, two = 0, curr, one
        return one