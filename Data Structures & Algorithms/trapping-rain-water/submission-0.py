class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                if lmax - height[l] > 0:
                    water += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                if rmax - height[r] > 0:
                    water += rmax - height[r]
        return water