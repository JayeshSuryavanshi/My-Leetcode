class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = {}
        pairs = 0
        for i in nums:
            if k - i in res and res[k - i] > 0:
                pairs += 1
                res[k - i] -= 1 
            elif i not in res:
                res[i] = 1
            else:
                res[i] += 1
        return pairs