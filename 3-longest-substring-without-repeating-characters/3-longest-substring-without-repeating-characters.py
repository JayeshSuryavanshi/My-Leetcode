class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        latest = {}
        l = 0
        max_length = 0
        for r in range(len(s)):
            if s[r] in latest:
                l = max(latest[s[r]], l)
            
            latest[s[r]] = r+1
            max_length = max(max_length, r-l+1)
        return max_length