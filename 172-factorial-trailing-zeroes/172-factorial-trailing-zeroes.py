class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(num):
            fact = 1
            for i in range(1, num+1):
                fact = fact * i
            return fact
        
        num_factorial = str(factorial(n))
        num_factorial = num_factorial[::-1]
        
        i = 0
        count = 0
        while i < len(num_factorial):
            if num_factorial[i] == '0':
                count += 1
                i += 1
            else:
                return count
        return count
            