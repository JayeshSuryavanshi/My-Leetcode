class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = collections.Counter(s)
        for idx in freq.keys():
            if freq[idx] == 1:
                return s.index(idx)
        return -1
        
        