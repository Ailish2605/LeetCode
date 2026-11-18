# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      
        if not root:
            return []

        res = []
        nodesStack = []
        nodesStack.append(root)

        rightToLeft = True

        while nodesStack:
            res.append([])
            curStack = nodesStack
            nodesStack = []

            rightToLeft = not rightToLeft

            while curStack:
                curNode = curStack.pop()
                res[-1].append(curNode.val)

                if rightToLeft:
                    
                    if curNode.right:
                        nodesStack.append(curNode.right)
                    if curNode.left:
                        nodesStack.append(curNode.left)
                else:
                    
                    if curNode.left:
                        nodesStack.append(curNode.left)
                    if curNode.right:
                        nodesStack.append(curNode.right)

        return res