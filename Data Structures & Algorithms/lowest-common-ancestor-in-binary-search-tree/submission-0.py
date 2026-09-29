# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.left < root.val and q.left < root.val:
            return self.lowestCommonAncestor(root.left)
        
        if p.right > root.val and q.right > root.val:
            return self.lowestCommo0nAncestor(root.right)
        
        return root