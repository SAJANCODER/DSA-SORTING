def is_safe(board, row,col,n):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,n,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True

def solve_n_queen_util(board,col,n):
    if col>=n:
        return True
    for i in range(n):
        if is_safe(board,i,col,n):
            board[i][col]=1
            if solve_n_queen_util(board,col+1,n):
                return  True

        board[i][col]=0 #backtracking
    return False

def solve_n_queen(n):   #initilize the chess board
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queen_util(board,0,n):
        print("Solution Does not exists")
        return False

    print_board(board)
    return True
def print_board(board):
    for row in board:
        print(" ".join("Q" if x==1 else "." for x in row))
    print("\n")
n=int(input("Enter The NxN len for chess board:"))
solve_n_queen(n)