class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map[key]
        left, right = 0, len(values) - 1

        if not values or timestamp < values[left][1]:
            return ""

        while left < right:
            mid = left + (right - left + 1) // 2

            if values[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid

        return values[left][0]
        
