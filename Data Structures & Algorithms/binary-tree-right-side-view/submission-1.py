# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ret = defaultdict(list)
        self.helper(root, 0)
        return [i[-1] for i in list(self.ret.values())]

    def helper(self, root, level):
        if root:
            self.ret[level].append(root.val)
            self.helper(root.left, level +1)
            self.helper(root.right, level+1)
            

        