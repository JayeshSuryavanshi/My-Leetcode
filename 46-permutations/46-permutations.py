class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, [], res)
        return res

    def helper(self, nums, temp, res):
        if len(nums) == 0:
            res.append(temp)
            return None
        for i in range(len(nums)):
            self.helper(nums[:i]+nums[i+1:],temp+[nums[i]],res)