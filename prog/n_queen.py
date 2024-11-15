def is_safe(board, row, col, n):
    # Check for queen in the same row to the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal to the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal to the left
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queen_util(board, col, n):
    # Base condition: All queens are placed
    if col >= n:
        return True

    # Place queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  # Place queen

            # Recur to place the rest of the queens
            if solve_n_queen_util(board, col + 1, n):
                return True

            # Backtrack: Remove the queen
            board[i][col] = 0

    return False


def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queen_util(board, 0, n):
        print("Solution does not exist.")
        return False

    print_board(board)
    return True


def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print("\n")


# Input and function call
n = int(input("Enter value of n: "))
solve_n_queens(n)
