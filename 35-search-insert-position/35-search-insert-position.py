class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle
        return left
                
                