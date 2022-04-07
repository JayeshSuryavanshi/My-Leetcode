class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mult = bin(int(bin(int(num1)), 2) * int(bin(int(num2)), 2))
        return str(int(mult, 2))