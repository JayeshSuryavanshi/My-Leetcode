from collections import Counter
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
#         nums = sorted(nums, reverse = True)
#         c = Counter(nums)
#         res = []
#         for item, cnt in c.items():
#             res.append(item)
        
#         if len(nums) < 4:
#             return res[2] 
#         else:
#             return max(res)
        res = []
        for i in nums:
            if i not in res:
                res.append(i)
        res.sort()
        return res[-3] if len(res)>=3 else res[-1]
        