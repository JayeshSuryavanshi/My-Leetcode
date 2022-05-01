class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for num in range(1,n+1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)
            if num % 3 == 0 and num % 5 == 0:
                ret.append("FizzBuzz")
            elif num % 3 == 0:
                ret.append("Fizz")
            elif num % 5 == 0:
                ret.append("Buzz")
            else:
                ret.append(str(num))
        return ret