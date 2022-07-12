class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Optimal Approach
        i = 0
        j = len(nums)-1
        
        squares = []
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                squares.insert(0,nums[j] ** 2)
                j -= 1
            else:
                squares.insert(0,nums[i] ** 2)
                i += 1
        return squares
                
          
        