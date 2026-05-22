class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        result = []
        for num, count in counter.items():
            heapq.heappush(result, (count, num))
            if len(result) > k:
                heapq.heappop(result)
        return [n for _, n in result]
                