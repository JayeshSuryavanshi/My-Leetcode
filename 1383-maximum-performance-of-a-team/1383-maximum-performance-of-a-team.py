class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        current_sum = 0
        h = []
        ans = -float('inf')
        
        for i, j in sorted(zip(efficiency, speed),reverse=True):
            while len(h) > k-1:
                current_sum -= heappop(h)
            heappush(h, j)
            current_sum += j
            ans = max(ans, current_sum * i)
            
        return ans % (10**9+7)
        