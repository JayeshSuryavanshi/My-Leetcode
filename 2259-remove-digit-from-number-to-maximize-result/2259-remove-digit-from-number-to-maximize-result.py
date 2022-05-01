class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = []
        for index,value in enumerate(number):
            curr = list(number)
            if value == digit:
                curr.pop(index)
                res.append(int(''.join(curr)))
        return str(max(res))

        