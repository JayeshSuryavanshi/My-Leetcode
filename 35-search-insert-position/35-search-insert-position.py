class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Using a binary search approach
        l, r = 0, len(nums)
        a = target
        while l < r:
            mid = (l + r) // 2
            if a > nums[mid]:
                l = mid + 1
            else:
                r = mid
        return l
                
                