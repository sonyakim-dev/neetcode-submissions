# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        result = []
        q = deque([root])

        while q:
            right = None
            for _ in range(len(q)):
                right = q.popleft()
                if right.left: q.append(right.left)
                if right.right: q.append(right.right)
            if right:
                result.append(right.val)
        
        return result