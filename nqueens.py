DIM = 8

def bprint(arr,b = None,r = None):
    for row in arr:
        for ele in row:
            print(ele,end=" ")
        print()


board = [[0 for _ in range(DIM)] for _ in range(DIM)]

def avaliable(board,x,y):
    if board[x][y] == 1:
        return False

    for i in range(DIM):
        if board[i][y] == 1:
            return False
    
    for j in range(DIM):
        if board[x][j] == 1:
            return False

    i,j = x + 1,y + 1
    while i < DIM and i > -1 and j < DIM and i > -1:
        if board[i][j] == 1:
            return False
        i += 1
        j += 1

    i,j = x - 1,y + 1
    while i < DIM and i > -1 and j < DIM and i > -1:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    i,j = x - 1,y - 1
    while i < DIM and i > -1 and j < DIM and i > -1:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i,j = x + 1,y - 1
    while i < DIM and i > -1 and j < DIM and i > -1:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    
    return True



def nqueen(board):
    queens = sum([sum(p) for p in board])
    if queens == DIM:
        bprint(board,1,0)
        print()
        return True

    else:
        for i in range(DIM):
            for j in range(DIM):
                if avaliable(board,i,j):
                    board[i][j] = 1
                    if nqueen(board):
                        return True

                    board[i][j] = 0
        
        return False
    

nqueen(board)
