class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '{':'}', '[':']'}
        stack = []
        
        for i in s:
            if i in pairs:
                stack.append(i)
            elif len(stack) == 0 or pairs[stack.pop()] != i:
                return False
        return len(stack) == 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # _ = {'(':')', '{':'}','[':']'}
        # stack = []
        # for i in s:
        #     if i in _:
        #         stack.append(i)
        #     elif len(stack) == 0 or _[stack.pop()] != i:
        #         return False
        # return len(stack) == 0 
        