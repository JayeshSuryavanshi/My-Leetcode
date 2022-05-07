class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
#         nums_cpy = sorted(nums)
#         print(nums)
#         print(nums_cpy)
#         if nums_cpy == nums:
#             return False
#         return True

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