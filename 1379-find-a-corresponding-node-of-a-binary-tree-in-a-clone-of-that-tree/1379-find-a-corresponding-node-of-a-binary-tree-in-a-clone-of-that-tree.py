class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if not original:
            # base case or stop condition:
            # empty node or empty tree
            return None
        
        #Handling general cases
        if original is target:
            
            # current original node is target, so it is cloned
            return cloned
        
        #Either left subtree has target or right subtree has target
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)