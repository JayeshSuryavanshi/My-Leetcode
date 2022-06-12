class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        result = i= total = 0
		
        for j in range(len(nums)):
            x = nums[j]   
            total += x
            counter[x] += 1
            while i < j and counter[x] > 1: 
                counter[nums[i]] -= 1
                total -= nums[i]
                i += 1
            
            result = max(result, total)            
        return result
        