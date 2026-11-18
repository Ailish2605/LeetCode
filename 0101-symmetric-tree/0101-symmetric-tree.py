class Solution:
    def isSymmetric(self, n: Optional[TreeNode]) -> bool:
        return bool((f:=lambda l,r:l==r==None or l and r and l.val==r.val 
            and f(l.left,r.right) and f(l.right,r.left))(n.left,n.right))