class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        prev_time = None
        for p, s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s
            if prev_time is None or time > prev_time:
                prev_time = time
                fleets += 1
        return fleets
