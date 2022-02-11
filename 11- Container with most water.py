class Solution:
    def maxArea(self, height: List[int]) -> int:
       
        area = 0
        i = 0
        j = len(height)-1
        
        while i < j:
            
            breath = j-i
            
            if height[i] < height[j]:
                length = height[i]
                i += 1
            else:
                length = height[j]
                j -= 1
            
            area = max(area, breath * length)
        
        return area