class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # is numbers sorted? NO, is there duplicates? NO
        l, r = 0, len(numbers)-1

        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return [l+1, r+1]