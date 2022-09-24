# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        stack = [(root, root.val, [root.val])] # stack stored with (root, sum, path)
        while stack:
            cur, Sum, path = stack.pop()
            if not cur.left and not cur.right:
                if Sum == targetSum:
                    ans.append(path)
            else:
                if cur.right:
                    stack.append((cur.right, Sum+cur.right.val, path+[cur.right.val]))                
                if cur.left:
                    stack.append((cur.left, Sum+cur.left.val, path+[cur.left.val]))
        return ans
        