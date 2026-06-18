class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # key: num, val: count
        # s = sorted(count.items(), key=lambda x: x[1], reverse=True)
        # return [n for n, _ in s[:k]]

        ## T.C = O(n log n), S.C: O(n)

        heap = []
        for n, c in count.items():
            heapq.heappush(heap, (c, n))
            if len(heap) > k:
                heapq.heappop(heap) # pop the smallest count

        return [n for c, n in heap]
        