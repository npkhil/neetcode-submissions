class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(0, 0)] * n
        for i in range(n):
            cars[i] = (position[i], speed[i])
        cars.sort(reverse = True)
        fleets = []
        for pos, speed in cars:
            time = (target - pos) / speed
            if fleets and time <= fleets[-1]:
                continue
            else:
                fleets.append(time)
        
        return len(fleets)
