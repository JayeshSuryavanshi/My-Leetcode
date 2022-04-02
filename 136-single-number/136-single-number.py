from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #initialize counter object 
        count = Counter(nums)
        
        # count.items() stores in element, count format
        for element, count in count.items():
            if count == 1:
                return(element)
        