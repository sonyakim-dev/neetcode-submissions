class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(s):
            if s in memo: return memo[s]
            if not s: return True

            for word in wordDict:
                if s.startswith(word) and dfs(s[len(word):]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False


        return dfs(s)