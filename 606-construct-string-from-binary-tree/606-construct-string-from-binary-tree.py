# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        _ = str(root.val)
        if root.left: 
            _ += "(" + self.tree2str(root.left) + ")"
        if root.right: 
            if not root.left: _ += "()"
            _ += "(" + self.tree2str(root.right) + ")"
        return _