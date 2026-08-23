# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        self.max = None
        self.helper(root)
        return max(self.max, root.val)

    def helper(self, root):
        if not root:
            return 0
        maxPath = 0
        leftLen = self.helper(root.left)
        rightLen = self.helper(root.right)
        maxLen = max(root.val, root.val + max(leftLen, rightLen))
        maxPath = max(maxLen, root.val+ leftLen+rightLen)
        if self.max == None or maxPath > self.max:
            self.max = maxPath
        return(maxLen)
        
        