class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        last day day is always 0 > start from the end of array
        """
        result = [0] * len(temperatures)
        stk = [] # (index, temp)

        for i, t in enumerate(temperatures):
            while stk and stk[-1][1] < t:
                index, temp = stk.pop()
                result[index] = i - index
            stk.append((i, t))
        return result