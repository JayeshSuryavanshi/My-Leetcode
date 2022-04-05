class Solution:
    def maxArea(self, height: List[int]) -> int:
        
#         line_height = len(height)
#         left, right = 0, line_height - 1
#         max_width = line_height - 1
#         area = 0
#         for width in range(max_width, 0, -1):
#             if height[left] < height[right]:
#                 area = max(area, width * height[left])
#                 left = left + 1
#             else:
#                 area = max(area, width * height[right])
#                 right = right - 1 
#         return area
        
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            res, l, r = max(res,  h * (r - l)), l + (height[l] == h), r - (height[r] == h)
        return res
        