class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        final = [''] * len(s)
        
        for i in range(len(s)):
            final[indices[i]] = s[i]
        return ''.join(i for i in final)
        
            
        
        
