class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isNonDecreasing = True
        isNonIncreasing = True
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                isNonDecreasing = False
            if nums[i] < nums[i-1]:
                isNonIncreasing = False
                
        return isNonDecreasing or isNonIncreasing
        