from itertools import permutations

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # nums are in descending order
        if i == 0:   
            nums.reverse()
            return 
           
        # finding the last ascending position
        k = i - 1 
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k] 
        
        # reverse the second part
        l, r = k+1, len(nums)-1  
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1

        
