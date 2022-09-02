# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        if not root:
            return []
        
        traversal_q = [root]
        average = []
        
        while traversal_q:
            cur_avg = sum( (node.val for node in traversal_q if node) ) / len(traversal_q)
            average.append( cur_avg )
            
            next_level_q = [ child for node in traversal_q for child in (node.left, node.right) if child ]
            
            traversal_q = next_level_q
            
        return average
        