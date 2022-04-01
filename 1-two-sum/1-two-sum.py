class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # checking if sum of both elements is equal to our target value 
                if (nums[i] + nums[j]) == target:
                    return i, j

