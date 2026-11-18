# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        q = deque([root])
        level = 0

        while q:
            size = len(q)
            level += 1

            for i in range(size):
                node = q.popleft()

                if not node.left and not node.right:
                    return level

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)