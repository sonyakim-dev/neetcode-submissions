class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ## DP - top-down
        # memo = {}

        # def dfs(s):
        #     if s == "": return True
        #     if s in memo: return memo[s]

        #     for word in wordDict:
        #         if s.startswith(word):
        #             if dfs(s[len(word):]):
        #                 memo[s] = True
        #                 return True
        #     memo[s] = False
        #     return False
        
        # return dfs(s)


        ## DP - bottom-up
        dp = [False] * (len(s) + 1) # whether the substring s[i:] can be segmented?
        dp[len(s)] = True # base case; empty string is valid

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]: break
        
        return dp[0]
