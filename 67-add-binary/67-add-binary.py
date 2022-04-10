class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # string -> int -> decimal
        A = int(a, 2)
        B = int(b, 2)
        sum = A + B
        # sum in binary format, then split at b, -1 is to return last element
        sum_binary = bin(sum).split('b')[-1]
        return sum_binary
        
        