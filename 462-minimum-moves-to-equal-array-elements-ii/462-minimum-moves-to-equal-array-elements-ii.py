class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        count = 0
        # sort nums in-place
        nums.sort() 
        mid = nums[len(nums)//2] 
        for num in nums:
            count += abs(mid-num)
        return count