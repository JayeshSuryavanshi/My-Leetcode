from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # counter object initialized as count
        count = Counter(s)
        
        # counter stores element:count(key)
        for indx in count.keys():
            if count[indx] == 1:
                return s.index(indx)
        return -1
