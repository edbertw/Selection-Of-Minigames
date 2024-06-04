s=int(input("Size--> "))
board,x=[[0 for i in range(s)]for x in range(s)],0
for i in range(s):
    for j in range(s):
        board[i][j]=x
        x=x+1
def printboard():
    for i in range(s):
        for j in range(s):
            if (j==s-1) and (board[i][j]=="X" or board[i][j]=="O"):print("",board[i][j])
            elif board[i][j]=='X' or board[i][j]=='O':print("",board[i][j],end=" ")
            elif (j==s-1) and board[i][j]<=9:print("",board[i][j])
            elif (j==s-1) and board[i][j]>9:print(board[i][j])
            elif board[i][j]<=9:print("",board[i][j],end=" ")
            else:print(board[i][j],end=" ")
def checkwin():
    for i in range(s):  #horizontal
        if board[i].count("X")==s or board[i].count("O")==s:return board[i][0],True
    verti,verti1,count1,count2,count3,count4=0,0,0,0,0,0
    for i in range(s):
        verti,verti1=0,0
        for x in range(s):
            if board[x][i]=='X':verti+=1
            elif board[x][i]=='O':verti1+=1
        if verti==s:return 'X',True
        elif verti1==s:return 'O',True
    for x in range(s):
        if board[x][x]=='X':count1+=1
        elif board[x][x]=='O':count2+=1
    if count1==s:return 'X',True
    elif count2==s:return 'O',True
    for x in range(s):
        if board[s-1-x][x]=='X':count3+=1
        elif board[s-1-x][x]=='O':count4+=1
    if count3==s:return 'X',True
    elif count4==s:return 'O',True
    return "" ,False
printboard()
currentplayer,counter,win='X',1,False
while win ==False:
    move=input(f"{currentplayer}--> ")
    for i in range(s):
        for j in range(s):
            if board[i][j]==int(move):board[i][j]=currentplayer  
    counter+=1
    printboard()
    if currentplayer=='X':currentplayer='O'
    elif currentplayer=='O':currentplayer='X'
    winner,win=checkwin()
    if counter>(s*s):break
    if win==True and winner!="":break
if win==True and winner!="":print("Winner:",winner)
elif win==False and winner=="" and counter>(s*s):print("Winner: None")
