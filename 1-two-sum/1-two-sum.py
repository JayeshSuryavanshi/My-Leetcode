class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for idx, value in enumerate(nums):
            remaining = target - nums[idx]
            if remaining in seen:
                return [seen[remaining], idx]
            else:
                seen[value] = idx
                
            
        
        