class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        def calculate_area(nums):
            n = len(nums)
            stack = []
            max_area = 0

            for i, val in enumerate(nums):
                if stack and val < stack[-1][0]:
                    while stack and val < stack[-1][0]:
                        a = stack.pop()
                        max_area = max(max_area, a[0] * (i - a[1]))
                    stack.append((val, a[1]))
                if not stack or val > stack[-1][0]:
                    stack.append((val, i))

            for i in stack:
                max_area = max(max_area, i[0] * (n - i[1]))

            return max_area

        rows, cols = len(matrix), len(matrix[0])
        prefix_sum = [[0] * cols for _ in range(rows)]

        for j in range(cols):
            prefix = 0
            for i in range(rows):
                if matrix[i][j] == '1':
                    prefix += 1
                else:
                    prefix = 0
                prefix_sum[i][j] = prefix

        max_area = 0
        for i in prefix_sum:
            max_area = max(max_area, calculate_area(i))

        return max_area