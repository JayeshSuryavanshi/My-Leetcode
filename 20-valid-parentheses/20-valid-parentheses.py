class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '{':'}', '[':']'}
        stack = []
        # "()[]{}"
        # "(]"
        for i in s:
            if i in pairs:
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif pairs[stack.pop()] != i:
                return False
        return len(stack) == 0
