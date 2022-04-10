class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A = int(a, 2)
        B = int(b, 2)
        sum = A + B
        sum_binary = bin(sum).split('b')[-1]
        return sum_binary
        
        