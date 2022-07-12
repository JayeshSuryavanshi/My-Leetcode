class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        square = lambda x: x ** 2
        
        for num in nums:
            squares.append(square(num))
        return sorted(squares)
        