class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # converted number to binary 
        num1 = bin(int(num1))
        num2 = bin(int(num2))
        # binaries cannot be added like normal addition; format different
        sum = bin(int(num1, 2) + int(num2, 2))
        return str(int(sum, 2))
        

        