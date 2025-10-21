# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """   
        PRE RDER : ROOT , LEFT , RIGHT
        
        """
        if not root:
            return []
        res = []
        res.append(root.val)
        if root.left:
            left_node = self.preorderTraversal(root.left)
            res.extend(left_node)
        if root.right:
            right_node = self.preorderTraversal(root.right)
            res.extend(right_node)
        return res
        
        