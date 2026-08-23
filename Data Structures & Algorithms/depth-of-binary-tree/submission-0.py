# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)
    def helper(self, root, h):
        if not root:
            return h
        else:
            h += 1
            return max(self.helper(root.left, h), self.helper(root.right, h))
        