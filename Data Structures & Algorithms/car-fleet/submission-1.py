class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)
        fleet = 1
        prev_time = (target - cars[0][0]) / cars[0][1]

        for i in range(1, len(cars)):
            pos, spd = cars[i]
            time = (target - pos) / spd
            if time > prev_time:
                fleet += 1
                prev_time = time

        return fleet