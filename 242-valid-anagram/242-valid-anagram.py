class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p = ''.join(sorted(s))
        q = ''.join(sorted(t))
        return p == q