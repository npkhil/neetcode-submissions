# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def aux(node):
          if not node:
            return (0, True)
          l_h, l_b = aux(node.left)
          r_h, r_b = aux(node.right)
          return (max(l_h, r_h) + 1, l_b and r_b and abs(l_h - r_h) <= 1)
        _, balance = aux(root)
        return balance