class Solution:
    def getRow(self, rowIndex: int) -> list[int]:

        return list(accumulate(range(1,rowIndex+2),
                    lambda x, y: x*(rowIndex+2 - y)//(y-1)))