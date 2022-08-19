class Solution:
    def search(self, nums: List[int], target: int) -> int:
            lo, hi = 0, None
            if not hi: hi = len(nums)
            pos = bisect_left(nums, target, lo, hi)
            return pos if pos != hi and nums[pos] == target else -1