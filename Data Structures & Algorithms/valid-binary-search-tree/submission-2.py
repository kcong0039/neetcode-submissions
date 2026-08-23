# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, None, None)
    def helper(self, node, hi, lo):
        if not node:
            return True
        if (hi != None and node.val >= hi) or (lo != None and node.val <= lo):
            return False
        return self.helper(node.left, node.val, lo) and self.helper(node.right, hi, node.val)
