# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        queue = deque([root])
        output = [root.val]

        while queue:
            level = len(queue)
            for i in range(level):
                node = queue.popleft()

                if i == level:
                    output.append(node.val)

                if node.left:
                    queue.append(node)
                
                if node.right:
                    queue.append(node)
        
        return output
                

            