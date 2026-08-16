# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      def aux(node):
        if node is None:
          return (0, 0)
        left_diameter, left_depth = aux(node.left)
        right_diameter, right_depth = aux(node.right)
        return (max(left_diameter, right_diameter, left_depth + right_depth), max(left_depth, right_depth) + 1)
      
      max_diameter, _ = aux(root)
      return max_diameter
    