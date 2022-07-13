from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = []
        for ele, cnt in c.most_common(k):
            freq.append(ele)
        return freq
            