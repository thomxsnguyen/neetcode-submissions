# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        goodNodes = 0
        
        def dfs(node, maxSoFar):
            nonlocal goodNodes

            if not node:
                return

            if node.val >= maxSoFar:
                goodNodes += 1

            maxSoFar = max(maxSoFar, node.val)

            
            left = dfs(node.left, maxSoFar)
            right = dfs(node.right, maxSoFar)
        
        dfs(root, root.val)
        return goodNodes
