import itertools
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sample = list(itertools.product([0,1], repeat = k))            
        return len({s[i:i + k] for i in range(len(s) - k + 1)}) == 2 ** k

        