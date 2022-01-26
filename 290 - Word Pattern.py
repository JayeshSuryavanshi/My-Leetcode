class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        a = pattern
        b = s.split()
        
        return map(a.find, a) == map(b.index, b)
        