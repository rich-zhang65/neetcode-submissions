class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]

        cars.sort(key=lambda x: (-x[0], x[1]))

        stack = []

        for c in cars:
            if not stack:
                stack.append(c)
            else:
                top = stack[-1]
                intersection = self.get_intersection(top, c)

                if not intersection or intersection[0] < 0 or intersection[1] > target:
                    stack.append(c)

        return len(stack)

    # returns (x, y) of intersecting point, or None if parallel. slopes are each (y-int, slope)
    def get_intersection(self, slope1: tuple(int, int), slope2: tuple(int, int)):
        b1, m1 = slope1
        b2, m2 = slope2

        if m1 == m2: return None

        x = (b2 - b1) / (m1 - m2)

        y = m1 * x + b1

        return x, y
        