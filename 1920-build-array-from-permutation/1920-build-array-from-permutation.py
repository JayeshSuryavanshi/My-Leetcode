class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [] * len(nums)
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
        