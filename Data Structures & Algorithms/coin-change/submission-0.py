class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(balance):
            if balance == 0:
                return 0
            if balance in memo:
                return memo[balance]
            
            result = amount + 1
            for coin in coins:
                if balance - coin >= 0:
                    result = min(result, dfs(balance - coin) + 1)
            memo[balance] = result
            return result

        result = dfs(amount)
        return result if result <= amount else -1