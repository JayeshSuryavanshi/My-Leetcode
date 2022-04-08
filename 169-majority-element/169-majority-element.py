from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = Counter(nums).most_common()[0][0]
        print(major)
        return major