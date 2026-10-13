# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        
        def dfs(node):
            nonlocal output
            if not node:
                return
            
            output.append(node.val)
            left = dfs(node.left)
            right = dfs(node.right)
            return node
        
        dfs(root)
        return output
            