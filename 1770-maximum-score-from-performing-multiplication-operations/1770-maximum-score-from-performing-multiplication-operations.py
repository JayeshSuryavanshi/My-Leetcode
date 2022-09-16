class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
    
                dp[i][left] = max (  multipliers[i] * nums[left]               + dp[i + 1][left + 1], 
                                     multipliers[i] * nums[n - 1 - (i - left)] + dp[i + 1][left]       )        
                
        return dp[0][0]