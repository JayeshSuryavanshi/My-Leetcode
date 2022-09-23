class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        modulo = 10**9 + 7
        for x in range(n):
            result = (result * (1 << (len(bin(x+1)) - 2)) + x+1) % modulo
        return result 