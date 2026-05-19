class Solution:
    def climbStairs(self, n: int) -> int:
        ## Dynamic Programming, Bottom Up
        # 0 -> 1 -> (2 -> 3) << identical
        #        -> 3
        #   -> (2 -> 3) << identical
        #        -> 4
        one = two = 1

        for _ in range(n-1):
            one, two = two, one + two
        return two