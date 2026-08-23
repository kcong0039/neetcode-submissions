# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.helper(root, root.val)
        return self.res
        
    def helper(self, node, max):
        if node:
            if node.val >= max:
                self.res += 1
                max = node.val
            self.helper(node.left, max)
            self.helper(node.right, max)

        