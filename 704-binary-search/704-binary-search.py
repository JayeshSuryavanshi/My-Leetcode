class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search Approach - TC: O(log(n))
#         left = 0
#         right = len(nums)-1
        
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] > target:
#                 right = mid - 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 return mid
#         return -1

            lo, hi = 0, None
            if not hi: hi = len(nums)
            pos = bisect_left(nums, target, lo, hi)
            return pos if pos != hi and nums[pos] == target else -1