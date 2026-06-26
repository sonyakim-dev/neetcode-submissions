class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0: return False

        target = total // 4
        side = [0, 0, 0, 0]
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if side[j] + matchsticks[i] <= target:
                    side[j] += matchsticks[i]

                    if dfs(i + 1): return True

                    side[j] -= matchsticks[i]
                    
                    if side[j] == 0: break

            return False

        return dfs(0)