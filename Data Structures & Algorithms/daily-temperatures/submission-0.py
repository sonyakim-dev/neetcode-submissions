class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        prev = [] # (temp, index)

        for i, t in enumerate(temperatures):
            while prev and t > prev[-1][0]:
                prev_t, prev_i = prev.pop()
                result[prev_i] = i - prev_i
            prev.append((t, i))

        return result