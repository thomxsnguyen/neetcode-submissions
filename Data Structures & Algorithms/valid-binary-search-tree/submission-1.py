# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        previous = None

        def inorder(node):
            nonlocal previous

            if node is None:
                return True
            
            if not inorder(node.left):
                return False
            
            if previous is not None and previous >= node.val:
                return False
            
            if not inorder(node.right):
                return False
            
            return node
            
        
        inorder(root)
        return root