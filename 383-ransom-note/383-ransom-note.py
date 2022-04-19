class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        return all(k in c2 and c2[k]>=c1[k] for k in c1)
        