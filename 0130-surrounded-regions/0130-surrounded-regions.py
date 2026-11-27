class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def mark(row,col):
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'O':
                board[row][col] = '*'
                mark(row-1,col)
                mark(row+1,col)
                mark(row,col-1)
                mark(row,col+1)

        for row in range(len(board)):
            mark(row,0)
            mark(row,len(board[0])-1)
        for col in range(len(board[0])):
            mark(0,col)
            mark(len(board)-1,col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == '*':
                    board[row][col] = 'O'