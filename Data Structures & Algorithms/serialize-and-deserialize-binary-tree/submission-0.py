# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.ret = ""
        self.helper(root, "")
        print(self.ret)
        return self.ret
    def helper(self, root, pre):
        if root:
            self.ret += pre+str(root.val)+"."
            self.helper(root.left, pre+"L")
            self.helper(root.right, pre+"R")
        
    

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nodes = {}
        ret = None
        print (data.split("."))
        for s in data.split(".")[:-1]:
            currNode = TreeNode(int(''.join(c for c in s if c.isdigit())))
            currLabel = ''.join(c for c in s if c.isalpha())
            nodes[currLabel] = currNode
            if currLabel == "":
                ret = currNode
                continue
            if currLabel[-1] == "L":
                nodes[currLabel[:-1]].left = currNode
            if currLabel[-1] == "R":
                nodes[currLabel[:-1]].right = currNode
        return ret
            



