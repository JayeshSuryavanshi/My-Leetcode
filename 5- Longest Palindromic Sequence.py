class Solution:
    def longestPalindrome(self, s: str) -> str:
        final = ""
        final_length = 0
        
        for i in range(len(s)):
            left, right = i, i
            
            while left >=0 and right < len(s) and s[left] == s [right]:
                if((right - left) + 1 > final_length):
                    final = s[left : right + 1]
                    final_length = right - left + 1
                    
                left -= 1
                right += 1
                
        for i in range(len(s)):
            left, right = i, i + 1
            
            while left >=0 and right < len(s) and s[left] == s [right]:
                if((right - left) + 1 > final_length):
                    final = s[left : right + 1]
                    final_length = right - left + 1
                    
                left -= 1
                right += 1
                
        return final
            