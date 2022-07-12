class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
        
#         l = len(nums)
#         while 0 in nums:
#             nums.remove(0)
#         while len(nums) < l:
#             nums.append(0)
                
        