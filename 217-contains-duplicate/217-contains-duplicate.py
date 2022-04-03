from collections import Counter 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for item, cnt in Counter(nums).items():
            if cnt > 1:
                return True
        return False