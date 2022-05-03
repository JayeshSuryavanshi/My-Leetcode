class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        
        x, y = len(nums) - 1, 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                x = min(x, i)
                y = max(y, i)
        return 0 if x >= y else y-x+1