class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## min-heap

        # counter = Counter(nums)
        # result = []
        # for num, count in counter.items():
        #     heapq.heappush(result, (count, num))
        #     if len(result) > k:
        #         heapq.heappop(result)
        # return [n for _, n in result]

        ## sort
        counter = Counter(nums)
        result = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return [n for n, _ in result[:k]]