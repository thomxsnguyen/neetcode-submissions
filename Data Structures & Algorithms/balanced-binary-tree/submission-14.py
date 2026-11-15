# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find_height(node):
            if not node:
                return 0
            
            left = find_height(node.left)
            right = find_height(node.right)

            return max(left, right) + 1

        if root is None:
            return True
        
        leftHeight = find_height(root.left)
        rightHeight = find_height(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

        
            
