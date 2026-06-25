class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # left > right
        result = []
        stk = []

        def dfs(left, right):
            if left == right == n:
                result.append(''.join(stk))
                return

            if left > right:
                stk.append(')')
                dfs(left, right + 1)
                stk.pop()
            if left < n:
                stk.append('(')
                dfs(left + 1, right)
                stk.pop()

        dfs(0, 0)
        return result