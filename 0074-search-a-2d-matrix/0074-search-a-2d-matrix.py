class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        r =  len(matrix)
        c =  len(matrix[0])
        total = r*c #no of elements: imagine them in 1D row now
        lo = 0 #put 2 pointers as if putting on a 1D row
        hi = total - 1 # total we calculated r*c = no of elements

        while lo <= hi:

            mid = lo + (hi - lo) // 2

            # Getting the Row and Index pointer
            rp = mid // c # divide the index by col size in a row
            cp = mid % c  # get the modulus to get the col pointer

            #Case 1: when number at [mid] < target: move to larger search space
            if matrix[rp][cp] < target:
                lo = mid + 1
            
            #Case 2: when number at [mid] > target: move to smaller search space
            elif matrix[rp][cp] > target:
                hi = mid -1
            
            #Case 3: found the number
            else:
                return True
        
        return False # Case 4: not found