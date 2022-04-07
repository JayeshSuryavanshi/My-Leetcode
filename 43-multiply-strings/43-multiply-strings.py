class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = bin(int(num1))
        num2 = bin(int(num2))
        mult = bin(int(num1, 2) * int(num2, 2))
        return str(int(mult, 2))