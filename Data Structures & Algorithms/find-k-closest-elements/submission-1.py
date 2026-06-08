class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # h = []
        # for a in arr:
        #     heapq.heappush(h, (-(abs(a - x)), -a))
        #     if len(h) > k:
        #         heapq.heappop(h)
        # return sorted([-(h[i][1]) for i in range(k)])

        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l+k]