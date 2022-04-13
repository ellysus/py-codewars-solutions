def is_solved(board):
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i] != 0 or board[i][0] == board[i][1] == board[i][2] != 0):
            return board[i][i]
        elif (board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0):
            return board[1][1]
    
    if sum(x.count(0) for x in board) > 0:
        return -1
    elif sum(x.count(0) for x in board) == 0:
        return 0