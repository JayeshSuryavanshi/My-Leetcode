from collections import Counter 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for item, cnt in c.items():
            if cnt > 1:
                return True
        return False