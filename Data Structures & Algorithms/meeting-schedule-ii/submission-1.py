"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        stack = []
        ans = 0

        heapq.heapify(stack)
        for i in intervals:
            while stack and stack[0] <= i.start:
                popped = heapq.heappop(stack)

            heapq.heappush(stack, i.end)
            ans = max(ans, len(stack))

        return ans
        