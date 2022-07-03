class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hills = 0
        valleys = 0
        
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                hills += 1
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                valleys += 1
        return (hills + valleys)
                
        