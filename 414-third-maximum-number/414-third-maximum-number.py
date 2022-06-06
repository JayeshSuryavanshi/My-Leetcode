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
        nums = sorted(set(nums), reverse=True)
        return nums[2] if len(nums) >= 3 else nums[0]
        