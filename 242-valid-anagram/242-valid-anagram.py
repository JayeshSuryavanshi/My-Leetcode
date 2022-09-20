class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = collections.Counter(s)
        count2 = collections.Counter(t)
        return count1 == count2