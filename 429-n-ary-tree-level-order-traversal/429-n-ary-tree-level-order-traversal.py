"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            temp = []
            for i in range(len(q)):
                node = q.pop(0)
                temp.append(node.val)
                for child in node.children:
                    if child:
                        q.append(child)
            ans.append(temp)
        return ans
        