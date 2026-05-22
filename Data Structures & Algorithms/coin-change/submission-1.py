class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## DP - top-down
        # memo = {} # key: amount, val: num of coins

        # def dfs(balance):
        #     if balance == 0:
        #         return 0
        #     if balance in memo:
        #         return memo[balance]

        #     result = amount
        #     for coin in coins:
        #         if balance - coin >= 0:
        #             result = min(result, dfs(balance - coin))
        #     memo[balance] = result
        #     return result

        # result = dfs(amount)
        # return result if result <= amount else -1


        ## DP - bottom-up
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # base case

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
