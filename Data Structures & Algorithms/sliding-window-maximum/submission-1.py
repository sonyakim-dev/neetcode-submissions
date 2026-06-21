class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1,2,1,0,4,2,6]
        #      i
        result = []
        # h = []

        # for i in range(len(nums)):
        #     heapq.heappush(h, (-nums[i], i))
        #     if i >= k - 1:
        #         while h[0][1] <= i - k:
        #             heapq.heappop(h)
        #         result.append(-h[0][0])

        ## Monotonically decreasing queue
        q = deque() # store index
        l = 0

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                result.append(nums[q[0]])
                l += 1

        return result