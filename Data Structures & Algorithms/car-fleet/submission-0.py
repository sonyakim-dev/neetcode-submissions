class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda a: a[0], reverse=True)
        count = 1
        prev_time = (target - cars[0][0]) / cars[0][1]

        for i in range(1, len(cars)):
            p, s = cars[i]
            time = (target - p) / s
            if time > prev_time:
                count += 1
                prev_time = time

        return count
