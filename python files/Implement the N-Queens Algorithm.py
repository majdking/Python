adj_matrix_1 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

adj_matrix_2 = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]


def display_adj_matrix(adj_matrix):
    for n in adj_matrix:
        print('\n')
        for e in n:
            if e == 1:
                print("Q", end='\t')
            else:
                print(e, end='\t')

def empty_adj_matrix_generator(n):
    """
    NxN rows and columns
    """
    adj_matrix = [[0]*n for _ in range(n)]
    return adj_matrix
    
# print(empty_adj_matrix_generator(4))

def is_safe(board, current_row, current_col):
    for row,column in enumerate(board):
        if current_row == row:
            return False
        elif current_col == column:
            return False
        elif abs(current_row - row) == abs(current_col - column):
            return False    
    return True

def dfs_n_queens(n):
    """
    Solves the N-Queens problem using a backtracking depth-first search approach.

    Args:
        n: The size of the chessboard (n x n) and the number of queens.

    Returns:
        A list of all possible solutions. Each solution is a list of integers,
        where the value at index `i` is the column of the queen in row `i`.
    """
    # User story 2: If n is less than 1, return an empty list
    if n < 1:
        return []
        
    solutions = []
    
    # Our recursive helper function
    def solve(current_row, board):
        # 1. BASE CASE: 
        # If current_row equals n, we have successfully placed all queens!
        # We need to add the current 'board' to our 'solutions'.
        if current_row == n:
            solutions.append(list(board))
        # 2. RECURSIVE STEP:
        # Loop through every possible column (from 0 to n-1).
        # Use our is_safe function.
        # If safe: Add the column to the board, call solve() for the next row, 
        # and then BACKTRACK (remove the column so we can try the next one).
        for current_column in range(n):
            if is_safe(board, current_row, current_column):
                board.append(current_column)
                solve(current_row + 1, board)
                board.pop()

    # Start the search at row 0 with an empty board
    solve(0, [])
    
    return solutions


print((dfs_n_queens(4)))