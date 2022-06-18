class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ctr = 0
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                ctr +=1 
            else:
                nums[i - ctr] = nums[i]
                
        return len(nums) - ctr
                
        
        
        
        