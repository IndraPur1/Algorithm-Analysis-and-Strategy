def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(1 - row):
            return False
    return True

def bactrack(row):
    if row == n:
        solution = []
        for i in range (n):
            line = ['.'] * n
            line[board[i]] = 'Q'
            solution.append(''.join(line))
        hasil.append(solution)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            backtrack(row + 1)
            board[row] = -1