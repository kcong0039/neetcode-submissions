# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        wl = deque()
        wl.append((root, 1))
        while wl:
            curr, currlvl = wl.popleft()
            if curr.left != None:
                wl.append((curr.left, currlvl+1))
            if curr.right != None:
                wl.append((curr.right, currlvl+1))
        return currlvl