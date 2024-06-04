def createBoard():
    global r
    global c
    r, c = 6, 7
    if 'n' == input('Standard game? (y/n): '):
        r, c = int(input('r? (2 - 20): ')), int(input('c? (2 - 20): '))
    return [['·'] * c for i in range(r)]

def printBoard(board):
    r, c = len(board), len(board[0])
    spaces = 1
    if r>9 or c>9: spaces = 2 #bigBoard
    x = ''
    for row in range(r-1,-1, -1):
        x += f'{row:>{spaces}}'
        ss = ' '
        if spaces==2: ss = '  '
        for col in range(c):
            x += ss+board[row][col]
        x += ' \n'
    x += ' ' + ' '*spaces
    for col in range(c): x += f'{col:>{spaces}}'+' '
    print(x)

def checkwin():
    for i in range(r):
        for j in range(c):
            if j+3<r and board[i][j]!='·' and board[i][j]==board[i][j+1] and board[i][j+1]==board[i][j+2] and board[i][j+2]==board[i][j+3]:
                return board[i][j],True
    for i in range(c):
        for j in range(r):
            if j+3<r and board[j][i]!='·' and board[j][i]==board[j+1][i] and board[j+1][i]==board[j+2][i] and board[j+2][i]==board[j+3][i]:
                return board[j][i],True
    for i in range(r-3):
        for j in range(c-3):
            if board[i][j]!='·' and board[i][j]==board[i+1][j+1] and board[i+1][j+1]==board[i+2][j+2] and board[i+2][j+2]==board[i+3][j+3]:
                return board[i][j],True
    for i in range(r-3):
        for j in range(c-3):
            if board[r-i-1][j]!='·' and board[r-i-1][j]==board[r-i-2][j+1] and board[r-i-2][j+1]==board[r-i-3][j+2] and board[r-i-3][j+2]==board[r-i-4][j+3]:
                return board[r-i-1][j],True
    return '',False
def makeMove(board, player, col):
    r = len(board)
    if board[-1][col]!='·':
        return False
    for row in range(r):
        if board[row][col]!='·' and board[row+1][col]=='·':
            board[row+1][col] = player
            break
        elif board[row][col]=='·':
            board[row][col] = player
            break
    return True
def validatemove(board,player,col):
    if col>c-1:
        return False
    else:
        return True
board = createBoard()
printBoard(board)
player = 'X'
counter=1
win=False
while True:
    move = input( 'player'+player+' (col #): ')
    if move == 'e':
        print("bye")
        exit()
    while validatemove(board,player,int(move))==False:
        printBoard(board)
        move = input( 'player'+player+' (col #): ')
        if move=='e':
            print("bye")
            exit()
    while makeMove(board, player, int(move))==False:
        printBoard(board)
        move = input( 'player'+player+' (col #): ')
        if move=='e':
            print("bye")
            exit()
    counter+=1
    printBoard(board)
    winner,win=checkwin()
    if player == 'X': player = 'O'
    else: player = 'X'
    if counter>(r*c):
        break
    if win==True and winner!="":
        break
if win==True and winner!="":
    print("Player",winner,"has won!") 
elif win==False and winner=="" and counter>(r*c):
    print("Draw!")
