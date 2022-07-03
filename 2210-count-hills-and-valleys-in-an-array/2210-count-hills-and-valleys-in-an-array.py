class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        HillValleyCount = 0
        
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                HillValleyCount += 1
            elif nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                HillValleyCount += 1
        return HillValleyCount
                
        