class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dictionary:
                return [i, dictionary[complement]]
            else:
                dictionary[nums[i]]=i
                
        