class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        l, r = 0, rows - 1

        while l < r:
            mid = (l + r) // 2

            max_col = 0
            for c in range(cols):
                if mat[mid][c] > mat[mid][max_col]:
                    max_col = c

            if mat[mid][max_col] < mat[mid + 1][max_col]:
                l = mid + 1
            else:
                r = mid

        max_col = 0
        for c in range(cols):
            if mat[l][c] > mat[l][max_col]:
                max_col = c

        return [l, max_col]