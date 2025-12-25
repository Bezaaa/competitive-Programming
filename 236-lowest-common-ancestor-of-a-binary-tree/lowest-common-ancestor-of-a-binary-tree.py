# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """ 
        Approach traverse left and right of ur tree 
        there are 3 possibilities 
        1.left has p or right has q or vice versa meaning they both return a val
        2. left return but right returns None
        3.right return but left returns None
       for the first case if not return meaning the current node is where they split  
        """
        if not root or p == root or q == root:
            return root
        left_tree = self.lowestCommonAncestor(root.left , p , q)
        right_tree = self.lowestCommonAncestor(root.right , p , q)
        if left_tree and right_tree:
            return root
        if left_tree and not right_tree:
            return left_tree
        else:
            return right_tree
      
        

       

      
        