from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        'Counter object for getting count'
        count = Counter(nums)
        for ele, cnt in count.items():
            'If count greater than 1 then duplicate exists'
            if (cnt > 1):
                return True
        return False
        
        
        
        