class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        line_height = len(height)
        left, right = 0, line_height - 1
        max_width = line_height - 1
        
        area = 0
        
        for width in range(max_width, 0, -1):
            
            # incrementing from left while calculating the area
            if height[left] < height[right]:
                area = max(area, width * height[left])
                left = left + 1
            
            # decrementing from right while calculating the area
            else:
                area = max(area, width * height[right])
                right = right - 1 
                
        return area
        
        
        