# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 
        def checkSymmetry(left_node , right_node):
            if not left_node and not right_node:
                return True
            if not left_node and right_node:
                return False
            if not right_node and left_node:
                return False
            if left_node.val != right_node.val:
                return False
            outer = checkSymmetry(left_node.left, right_node.right)
            inner = checkSymmetry(left_node.right, right_node.left)
            
            return outer and inner
        return checkSymmetry(root.left , root.right)
         

       
            
        
      
      

        