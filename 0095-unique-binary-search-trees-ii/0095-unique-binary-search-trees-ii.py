# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        def f(start,end):
            if start > end:
                return [None]
            ans = []
            for i in range(start,end+1):
                l = f(start,i-1)
                r = f(i+1,end)
                for x in l:
                    for y in r: 
                        root = TreeNode(i)
                        root.left = x
                        root.right = y
                        ans.append(root)
            return ans
        return f(1,n)