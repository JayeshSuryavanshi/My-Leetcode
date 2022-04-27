class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in mapping:
                stack.append(i)
            elif len(stack) == 0 or mapping[stack.pop()] != i:
                return False
        return len(stack) == 0 
        