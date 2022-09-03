class Solution:
    def reverse(self, x: int) -> int:
        number = "".join(reversed(list(str(abs(x)))))
        result = int("-" + number) if x < 0 else int(number)
        if -2**31 <= result <= (2**31)-1:
            return result
        else:
            return 0