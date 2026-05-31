class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if len(count) <= 2: continue

            n_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    n_count[n] = c - 1
            count = n_count
        
        result = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                result.append(n)
        return result