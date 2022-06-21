class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        furthest = 0
        q = []
        for i in range(1, len(heights)):
            delta = heights[i] - heights[i-1]
            if delta > 0:
                heapq.heappush(q, delta)
                if ladders == 0:
                    bricks -= heapq.heappop(q)
                else:
                    ladders -= 1
                if bricks < 0:
                    return i - 1
        return len(heights)-1