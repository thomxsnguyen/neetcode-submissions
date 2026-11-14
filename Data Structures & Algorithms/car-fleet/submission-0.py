class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(positions)):
            cars.append((positions[i], speed[i]))
        
        cars.sort(reverse=True)

        stack = []

        for position, speed in cars:
            time = (target - position) / speed
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        
        return len(stack)
