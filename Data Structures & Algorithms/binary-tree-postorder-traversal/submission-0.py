# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        
        def dfs(node):
            nonlocal output
            if not node:
                return
            
            left = dfs(node.left)
            right = dfs(node.right)
            output.append(node.val)
            return node
        
        dfs(root)
        return output
            