class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        neg = float(-inf)
        rev = nums[::-1]
        for i in rev:
            if i < neg: 
                return True
            while stack and i > stack[-1]: 
                neg = stack.pop()
            stack.append(i)
        return False