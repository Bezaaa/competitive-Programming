# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 
        i go left and i go right if both return a value the current node is the ancestor
        if one return a val then the val is the node
        """

        if not root or p ==root or q==root:
            return root
     


        left = self.lowestCommonAncestor(root.left , p , q)
        right = self.lowestCommonAncestor(root.right , p , q)
        if left and right:
            return root
        if left and not right:
            return left
        else:
            return right
        
        
            
        
