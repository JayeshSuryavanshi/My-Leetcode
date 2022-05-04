class Solution:
    def mySqrt(self, x: int) -> int:
        k = x
        x = (k + 1)/4.0
        y = x * x
        
        diff = y - k
        e = 0.5
        
        while diff < -e or diff > e:
            x = x + (k - y) / (2 * x)
            y = x * x
            diff = y - k
        
        return int(x)
        