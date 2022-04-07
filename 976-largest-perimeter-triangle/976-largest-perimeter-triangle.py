class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        while len(nums) > 2:
            triangle = nums[-3:]
            if sum(triangle[:2]) > triangle[-1]:
                return sum(triangle)
            else:
                nums.pop()
        return 0
        