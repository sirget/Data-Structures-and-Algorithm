def issafe(board,r,c):
    tmp = r
    while(tmp>=0):
        tmp -= 1
        if(board[tmp][c]):
            return False
    tmp = r 
    while(r<8 and c>= 0):


def putQ(board,r):
    for c in range(8):
        if(issafe(board,r,c)):
            board[r][c] = 1
            if(r == 7):
                print(board)
            else:
                putQ(board,r+1)
            board[r][c] = 0
