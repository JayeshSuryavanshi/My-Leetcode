class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = 0
        sum = 0
        for i in s[::-1]:
            curr = hashmap[i]
            if prev > curr:
                sum = sum - curr
            else:
                sum = sum + curr
            prev = curr
        return sum