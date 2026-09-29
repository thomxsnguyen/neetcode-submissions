# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not p and not q:
            return
    
        if not root:
            return
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p.left, q.left)
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommo0nAncestor(root.right, p.right, q.right)
        
        return root