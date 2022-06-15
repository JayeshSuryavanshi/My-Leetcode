class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}
        
        for i in range(len(nums)):
            if target-nums[i] in dictionary:
                return [i , dictionary[target-nums[i]]]
            dictionary[nums[i]] = i

#             nums = sorted(nums)
#             left, right = 0, len(nums)-1

#             while left < right:
#                 currentSum = nums[left] + nums[right]
#                                 # 2   + 4 = 6
#                 if currentSum == target:
#                     return [left, right]

#                 if target > currentSum:
#                     left += 1
#                 elif target < currentSum:
#                     right -=1
#                 else:
#                     break

#             return[-1,-1]