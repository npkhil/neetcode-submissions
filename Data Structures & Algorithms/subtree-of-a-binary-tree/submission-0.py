# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equivTree(p, q):
          if not p and q or not q and p:
            return False
          if not p and not q:
            return True
          return equivTree(p.left, q.left) and equivTree(p.right, q.right) and p.val == q.val
        
        if root and subRoot:
          return equivTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        if not root and not subRoot:
          return True
        return False