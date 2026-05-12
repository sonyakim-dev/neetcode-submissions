class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        h = []

        for val, ct in count.items():
            if len(h) < k: # only keep the heap size upto k
                heapq.heappush(h, (ct, val))
            elif ct > h[0][0]: # h[0][0]: the smallest val in heap
                heapq.heappop(h)
                heapq.heappush(h, (ct, val))
        
        return [val for _, val in h]

        