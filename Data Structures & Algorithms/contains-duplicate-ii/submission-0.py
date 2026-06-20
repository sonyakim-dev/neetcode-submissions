class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = defaultdict(list)
        for i in range(len(nums)):
            indices = record[nums[i]]
            if indices and abs(indices[-1] - i) <= k:
                return True
            indices.append(i)

        return False