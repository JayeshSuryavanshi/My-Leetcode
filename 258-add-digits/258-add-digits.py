class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            result = 0
            while num:
                result = result + num % 10
                num = num // 10
            num = result
        return num