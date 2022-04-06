class Solution:
    def climbStairs(self, n: int) -> int:
        a , b = 1, 1
        
        # _ denotes 'for everything in'
        for _ in range(n):
            a, b = b, a + b
        return a
        