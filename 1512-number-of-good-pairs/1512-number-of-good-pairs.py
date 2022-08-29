class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numset = set(nums)
        count = 0
        
        if len(numset) == len(nums):
            return 0
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
                    
        