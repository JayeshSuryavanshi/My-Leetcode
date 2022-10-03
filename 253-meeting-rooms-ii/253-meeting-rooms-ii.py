class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key=lambda x: x[0])
        for x, y in intervals:
            if not heap or heap[0] > x:
                heapq.heappush(heap, y)
            else:
                heapq.heappushpop(heap,y)

        return len(heap)