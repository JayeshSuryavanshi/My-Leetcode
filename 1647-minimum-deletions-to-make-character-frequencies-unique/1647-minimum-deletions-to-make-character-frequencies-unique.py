from collections import Counter 
class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        count = 0
        unique = set()
        for elem, cnt in c.items():
            while cnt > 0 and cnt in unique:
                cnt -= 1
                count += 1
            unique.add(cnt)
        return count 
        