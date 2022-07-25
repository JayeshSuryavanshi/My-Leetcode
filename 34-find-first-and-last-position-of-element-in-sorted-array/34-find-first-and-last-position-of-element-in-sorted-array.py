class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            left, right = 0, len(nums)           
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid+1
                else:
                    right = mid                    
            return left
        
        left = search(target)
        right = search(target+1)-1
        
        if left <= right:
            return [left, right]
                
        return [-1, -1]
                
        