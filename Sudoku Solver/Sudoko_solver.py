#Solver
#-------------------------------------------------
def print_board(board):
    for row in range(len(board)):
        if row%3 == 0 and row != 0:
            print('-----------------------------------')
        for col in range(len(board)):
            if col%3 == 0 and col != 0:
                print(' | ',end='')
            print(' ',board[row][col],end='')
        print('\n')
#--------------------------------------------------
def is_empty(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return (row,col)
    return False
#------------------------------------------------------
def check(board,num,p):
    #check row, p=(row,col)
    for row in range(len(board)):
        if num == board[row][p[1]] and row != p[0]:
            return False
    #check col
    for col in range(len(board)):
        if num == board[p[0]][col] and col != p[1]:
            return False
    #check cube
    r=(p[0]//3)*3
    c=(p[1]//3)*3
    for i in range(r,r+3):
        for j in range(c,c+3):
            if board[i][j] == num and (i,j) != p:
                return False
    return True
#------------------------------------------------------
def solve(board):
    pos = is_empty(board)
    if not(pos):
        return True
    else:
        x , y = pos
    for i in range(1,10):
        if check(board,i,(x,y)):
            board[x][y]=i
            if solve(board):
                return True
            board[x][y]=0
    return False





