class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        fleets = 0
        curr_fleet = None

        for c in cars:
            if not curr_fleet:
                curr_fleet = c
                fleets += 1
            else:
                intersection = self.get_intersection(curr_fleet, c)

                if not intersection or intersection[0] < 0 or intersection[1] > target:
                    curr_fleet = c
                    fleets += 1

        return fleets

    # returns (x, y) of intersecting point, or None if parallel. slopes are each (y-int, slope)
    def get_intersection(self, slope1: tuple(int, int), slope2: tuple(int, int)):
        b1, m1 = slope1
        b2, m2 = slope2

        if m1 == m2: return None

        x = (b2 - b1) / (m1 - m2)

        y = m1 * x + b1

        return x, y
        