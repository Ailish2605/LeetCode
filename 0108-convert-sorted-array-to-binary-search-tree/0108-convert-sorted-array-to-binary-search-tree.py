class Solution: 
    def sortedArrayToBST(self, n: list[int]) -> TreeNode:

        if not n: return None                                           
        m = len(n)//2

        return TreeNode(n[m],self.sortedArrayToBST(n[:m]),             
                             self.sortedArrayToBST(n[m+1:]))           