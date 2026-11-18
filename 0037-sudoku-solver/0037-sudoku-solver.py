class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isSafe(row, col, num):
            for i in range(9):
                if board[row][i] == num:
                    return False
                if board[i][col] == num:
                    return False

            start_row = (row // 3) * 3
            start_col = (col // 3) * 3

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False

            return True

        def solve():

            best_row = -1
            best_col = -1
            best_options = None

            for row in range(9):
                for col in range(9):

                    if board[row][col] == ".":

                        options = []

                        for num in "123456789":
                            if isSafe(row, col, num):
                                options.append(num)

                        if len(options) == 0:
                            return False

                        if best_options is None or len(options) < len(best_options):
                            best_options = options
                            best_row = row
                            best_col = col

                            if len(options) == 1:
                                break

                if best_options is not None and len(best_options) == 1:
                    break

            if best_options is None:
                return True

            for num in best_options:

                board[best_row][best_col] = num

                if solve():
                    return True

                board[best_row][best_col] = "."

            return False

        solve()