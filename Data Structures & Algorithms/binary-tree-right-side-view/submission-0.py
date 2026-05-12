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
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            el = None
            for _ in range(size):
                el = q.popleft()
                if el.left: q.append(el.left)
                if el.right: q.append(el.right)
            if el:
                result.append(el.val)
        
        return result