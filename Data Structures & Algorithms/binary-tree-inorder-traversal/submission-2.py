# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def dfs(node):
            nonlocal output

            if not node:
                return
            
            left = dfs(node.left)

            output.append(node.val)

            right = dfs(node.right)

            return node
        
        dfs(root)

        return output
