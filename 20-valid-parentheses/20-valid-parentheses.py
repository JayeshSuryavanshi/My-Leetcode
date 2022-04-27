class Solution:
    def isValid(self, s: str) -> bool:
        _ = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in _:
                stack.append(i)
            elif len(stack) == 0 or _[stack.pop()] != i:
                return False
        return len(stack) == 0 
        