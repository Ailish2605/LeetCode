class Solution:
    def subsetsWithDup(self, n):
        n.sort(); a, l = [[], [n[0]]], 1
        for i, x in enumerate(n[1:]):
            l, r = len(a), l
            a += [s + [x] for s in a[r if n[i] == x else 0:l]]
        return a