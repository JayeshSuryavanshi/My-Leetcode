from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        sample = []
        print(c.most_common(k))
        for ele, cnt in c.most_common(k):
            sample.append(ele)
        return sample
            