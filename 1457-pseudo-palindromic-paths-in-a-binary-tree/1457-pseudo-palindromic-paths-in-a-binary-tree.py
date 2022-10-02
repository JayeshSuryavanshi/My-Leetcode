# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        target = {0, 1, 2, 4, 8, 16, 32, 64, 128, 256}
        def dfs(x, s):
            s ^= 1 << (x.val - 1)
            if not x.left and not x.right:
                return int(s in target)
            return (dfs(x.left, s) if x.left else 0) + (dfs(x.right, s) if x.right else 0)
        return dfs(root, 0)