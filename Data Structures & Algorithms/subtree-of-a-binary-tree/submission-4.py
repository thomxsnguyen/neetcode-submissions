# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        tree1 = []
        tree2 = []

        def dfs(node, output):
            if not node:
                return
            
            
            left = dfs(node.left, output)
            output.append(node.val)
            right = dfs(node.right, output)

            return node
        
        dfs(root, tree1)
        dfs(subRoot, tree2)

        if tree2 in tree1:
            return True
        return False

        