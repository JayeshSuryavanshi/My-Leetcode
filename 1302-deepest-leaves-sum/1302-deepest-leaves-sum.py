# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
                dic = {}
                def DFS(root,counter):
                    if not root:
                        return 0
                    if not root.left and not root.right:
                        if counter in dic:
                            dic[counter].append(root.val)
                        else:
                            dic[counter]=[root.val]
                    DFS(root.left,counter+1)
                    DFS(root.right,counter+1)
                DFS(root,0)
                return sum(dic[max(dic)])
