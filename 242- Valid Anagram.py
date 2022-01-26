class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        if sorted_s == sorted_t:
            return True
    