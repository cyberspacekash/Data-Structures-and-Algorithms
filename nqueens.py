class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]

    def print_solution(self):
        for row in self.board:
            print(row)

    def is_safe(self, row, col):
        # check the row
        for i in range(col):
            if self.board[row][i]:
                return False
        # check the upper diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j]:
                return False
        # check the lower diagonal
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j]:
                return False
        return True

    def solve(self, col):
        # base case: all queens are placed
        if col == self.n:
            return True
        # try to place the queen in each row of the current column
        for row in range(self.n):
            if self.is_safe(row, col):
                # place the queen and recursively solve the next column
                self.board[row][col] = 1
                if self.solve(col+1):
                    return True
                # if the solution was not found, backtrack and remove the queen
                self.board[row][col] = 0
        return False
n = 8  
queens = NQueens(n)
if queens.solve(0):
    queens.print_solution()
else:
    print("No solution exists.")
