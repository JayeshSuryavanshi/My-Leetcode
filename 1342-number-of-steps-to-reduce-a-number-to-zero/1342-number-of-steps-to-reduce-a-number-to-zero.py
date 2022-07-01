class Solution:
    def numberOfSteps (self, num: int) -> int:
        bs = bin(num)[2:]
        return len(bs) - 1 + bs.count('1')