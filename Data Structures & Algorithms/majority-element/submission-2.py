class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## Boyer-Moore Voting Algorithm
        ## Since the maj el appears more than half the time,
        ## inc count when a candidad appears, else dec. if count = 0, pick a new cand
        el, count = 0, 0
        for n in nums:
            if count == 0:
                el = n
            if n == el:
                count += 1
            else:
                count -= 1
        return el
        
        # maj = len(nums) / 2
        # counter = defaultdict(int)

        # for n in nums:
        #     counter[n] += 1
        #     if counter[n] > maj: return n