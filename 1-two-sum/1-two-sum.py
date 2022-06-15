class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        
#         for num in nums:
#             potentialMatch = target - num
#             if potentialMatch in hashset:
#                 return [nums.index(potentialMatch), nums.index(num)]
#             else:
#                 hashset[num] = True
                
#         return []
        
        dictionary = {}
        
        for i in range(len(nums)):
            if target-nums[i] in dictionary:
                return [i , dictionary[target-nums[i]]]
            dictionary[nums[i]] = i

