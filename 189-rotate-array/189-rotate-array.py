class Solution(object):
    def rotate(self, nums, k):
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]