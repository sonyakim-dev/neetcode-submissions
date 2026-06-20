class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # [1, 2, 2, 3, 3]
        boats = 0
        l, r = 0, len(people) - 1

        while l <= r:
            if l != r and people[l] + people[r] > limit:
                boats += 1
                r -= 1
            else:
                boats += 1
                l += 1
                r -= 1
        return boats