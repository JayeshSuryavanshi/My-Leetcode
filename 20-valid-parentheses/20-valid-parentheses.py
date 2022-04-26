class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')', '{':'}','[':']'}
        stack = []
        for bracket in s:
            if bracket in mapping:
                stack.append(bracket)
            elif len(stack) == 0 or mapping[stack.pop()] != bracket:
                return False
        return len(stack) == 0 
        