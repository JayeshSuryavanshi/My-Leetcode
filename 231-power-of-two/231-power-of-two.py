class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        number = n
        complement = (n & n - 1)
        return number and not complement
            
        