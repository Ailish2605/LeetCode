class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        x = set(nums)
        xx = []

        for i in range(1,len(nums)+1):
            if i not in x:
                xx.append(i)
        return xx
        