# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        dq = deque([root])
        res = []
        flg = -1

        while dq:
            level = deque()
            flg = -flg

            for _ in range(len(dq)):
                node = dq.popleft()

                if flg > 0:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            res.append(list(level))

        return res


        