# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def dfs(node):
            if not node: return 0
            return max(dfs(node.left) + 1, dfs(node.right) + 1)
        
        l, r = dfs(root.left), dfs(root.right)
        if abs(l - r) > 1: return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)