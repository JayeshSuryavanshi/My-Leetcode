class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            y = target - nums[i]
            if y in hashmap:
                return [i, hashmap[y]]
            else:
                hashmap[nums[i]] = i