from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        count = Counter(nums)
        for ele, cnt in count.items():
            if (cnt > 1):
                return True
        return False
        
        
        
        