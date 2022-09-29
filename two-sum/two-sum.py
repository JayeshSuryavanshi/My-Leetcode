class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            potentialMatch = target - nums[i]
            if potentialMatch in dictionary:
                return [dictionary[potentialMatch], i]
            else:
                dictionary[nums[i]] = i

            