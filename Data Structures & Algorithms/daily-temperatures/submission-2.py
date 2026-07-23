class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stk = [] # (i, temp)

        for i, temp in enumerate(temperatures):
            while stk and stk[-1][1] < temp:
                j, t = stk.pop()
                result[j] = i - j
            stk.append((i, temp))

        return result