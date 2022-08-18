class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        final = [''] * len(s)
        _ = ''
        for i in range(len(s)):
            final[indices[i]] = s[i]
        
        for j in final:
            _ += j
            
        return _
        
            
        
        
