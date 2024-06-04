chess=[['br','bn','bb','bq','bk','bb','bn','br'],['bp']*8,['--']*8,['--']*8,['--']*8,['--']*8,['wp']*8,['wr','wn','wb','wq','wk','wb','wn','wr']]
ndict={'8':0,'7':1,'6':2,'5':3,'4':4,'3':5,'2':6,'1':7}
ldict={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
def printboard(chess):
    x=8
    for i in range(len(chess)):
        print(str(x)+'.',end=' ')
        for j in range(8):
            if j==7:
                print(chess[i][j])
            else:
                print(chess[i][j],end=' ')
        x-=1
    print('   a. b. c. d. e. f. g. h.')
    
def validposition(x):
    return x[8] in 'abcdefgh' and x[10] in '12345678'

def validmove(x):
    return x[3]==x[8] and x[5]==x[10]

def pawnmove(chess,piece,sr,sc,er,ec):
    if chess[sr][sc][0]==chess[er][ec][0]:
        return False
    if chess[sr][sc][0]=='w':
        if sr==6 and (er==4 or er==5) and sc==ec and chess[sr][sc]=='wp' and chess[er][ec]=='--':
            return True
    elif chess[sr][sc][0]=='b':
        if sr==1 and (er==2 or er==3) and sc==ec and chess[sr][sc]=='bp' and chess[er][ec]=='--':
            return True
    if (chess[sr][sc][0]=='w' and er-sr==-1 and sc==ec and chess[er][ec]=='--') or (er-sr==-1 and abs(ec-sc)==1 and chess[er][ec][0]=='b' ):
            return True
    if (chess[sr][sc][0]=='b' and er-sr==1 and sc==ec and chess[er][ec]=='--') or (er-sr==1 and abs(ec-sc)==1 and chess[er][ec][0]=='w'):
            return True
    return False
    
def knightmove(chess,piece,sr,sc,er,ec):
    if chess[sr][sc][0]==chess[er][ec][0]:
        return False
    if chess[sr][sc][0]=='w' and abs(sc-ec)==2 and abs(sr-er)==1 and chess[er][ec][0]!='w':
         return True
    elif chess[sr][sc][0]=='w' and abs(sc-ec)==1 and abs(sr-er)==2 and chess[er][ec][0]!='w':
        return True
    elif chess[sr][sc][0]=='b' and abs(sc-ec)==2 and abs(sr-er)==1 and chess[er][ec][0]!='b':
        return True
    elif chess[sr][sc][0]=='b' and abs(sc-ec)==1 and abs(sr-er)==2 and chess[er][ec][0]!='b':
        return True
    return False

def bishopmove(chess,piece,sr,sc,er,ec):
    if chess[sr][sc][0]==chess[er][ec][0]:
        return False
    if abs(sr-er)==abs(sc-ec):
        if er<sr:
            rstep=-1
        else:
            rstep=1
        if ec<sc:
            cstep=-1
        else:
            cstep=1
        r=sr+rstep
        c=sc+cstep
        while r!=er and c!=ec and r>=0 and r<=7 and c>=0 and c<=7:
            if chess[r][c]!="--":
                return False
            r+=rstep 
            c+=cstep
        return True
    else:return False
def rookmove(chess,piece,sr,sc,er,ec):
    if sr==er:
        s=min(sc,ec)+1
        e=max(sc,ec)
        for i in range(s,e):
            if chess[sr][i]!='--':
                return False 
    if sc==ec:
        s=min(sr,er)+1
        e=max(sr,er)   
        for i in range(s,e):
            if chess[i][sc]!='--':
                return False
    if er>=0 and er<=7 and ec>=0 and ec<=7 and chess[sr][sc][0]=='w' and (sc==ec or sr==er) and chess[er][ec][0]!='w':
        return True
    if er>=0 and er<=7 and ec>=0 and ec<=7 and chess[sr][sc][0]=='b' and (sc==ec or sr==er) and chess[er][ec][0]!='b':
        return True
    return False

def queenmove(chess,piece,sr,sc,er,ec):
    if chess[sr][sc][0]==chess[er][ec][0]:
        return False
    if rookmove(chess,piece,sr,sc,er,ec)==True or bishopmove(chess,piece,sr,sc,er,ec)==True:
        return True
    return False

def kingmove(chess,piece,sr,sc,er,ec):
    if sr==er and sc==ec:
        return False
    if chess[sr][sc][0]==chess[er][ec][0]:
        return False
    if er>=0 and er<=7 and ec>=0 and ec<=7 and chess[sr][sc][0]=='w' and abs(ec-sc)<=1 and abs(er-sr)<=1 and chess[er][ec][0]!='w':
        return True
    if er>=0 and er<=7 and ec>=0 and ec<=7 and  chess[sr][sc][0]=='b' and abs(ec-sc)<=1 and abs(er-sr)<=1 and chess[er][ec][0]!='b':
        return True
    return False

def findking(bo,cturn):
    for i in range(8):
        for j in range(8):
            piece=cturn+'k'
            if bo[i][j]==piece:
                return [i,j]

def kingcheck(chess,rturn):
    global killer
    kp=findking(chess,rturn)
    if rturn=='w':
        turn='b'
    elif rturn=='b':
        turn='w'
    for r in range(8):
        for c in range(8):
            if chess[r][c][0]==turn:
                if valid1move(chess,chess[r][c],r,c,kp[0],kp[1]):
                    killer=[r,c]
                    return True
    return False
def escape(chess,rturn,turn):
    kp=findking(chess,rturn)
    for i in range(8):
        for j in range(8):
            if valid1move(chess,rturn+'k',kp[0],kp[1],i,j) == True:
                simulate=[r.copy() for r in chess]
                simulate[kp[0]][kp[1]] = '--'
                simulate[i][j] = rturn+'k'
                if kingcheck(simulate,rturn)==False:
                    #printboard(simulate)
                    return False
    return True

def block(chess,rturn,turn):
    for i in range(8):
        for j in range(8):
            blockerturn=chess[i][j][0]
            blockertype=chess[i][j][-1]
            if blockerturn == rturn and blockertype != 'k':
                for a in range(8):
                    for b in range(8):
                        if valid1move(chess,blockerturn+blockertype,i,j,a,b) == True:
                            simulate=[r.copy() for r in chess]
                            simulate[i][j]='--'
                            simulate[a][b]=blockerturn+blockertype
                            if kingcheck(simulate,rturn)==False:
                                #printboard(simulate)
                                return False
    return True

def kill(chess,rturn,turn):
    for i in range(8):
        for j in range(8):
            if chess[i][j][0]==rturn:
                killmove=chess[i][j]
                if valid1move(chess,chess[i][j],i,j,killer[0],killer[1]):
                    simulate=[r.copy() for r in chess]
                    simulate[i][j]='--'
                    simulate[killer[0]][killer[1]]=killmove
                    if kingcheck(simulate,rturn)==False:
                        #printboard(simulate)
                        return False
    return True
def checkmate(chess,rturn,turn):
    #king in check state
    if kingcheck(chess,rturn) == False:
        return False
    #escape
    if escape(chess,rturn,turn) == False:
        return False
    #block
    if block(chess,rturn,turn) == False:
        return False
    #kill
    if kill(chess,rturn,turn) == False:
        return False              
    return True
    
def valid1move(chess,piece,sr,sc,er,ec):
    if piece!=chess[sr][sc]:
        return False
    if chess[sr][sc][0]=='w' and chess[er][ec][0]=='w':
        return False
    if chess[sr][sc][0]=='b' and chess[er][ec][0]=='b':
        return False
    if chess[sr][sc][1]=='p':
        return pawnmove(chess,piece,sr,sc,er,ec)
    elif chess[sr][sc][1]=='r':
        return rookmove(chess,piece,sr,sc,er,ec)
    elif chess[sr][sc][1]=='b':
        return bishopmove(chess,piece,sr,sc,er,ec)
    elif chess[sr][sc][1]=='n':
        return knightmove(chess,piece,sr,sc,er,ec)
    elif chess[sr][sc][1]=='q':
        return queenmove(chess,piece,sr,sc,er,ec)
    elif chess[sr][sc][1]=='k':
        return kingmove(chess,piece,sr,sc,er,ec)
    return False
killer=[]
moves=input().split()
printboard(chess)
turn,rturn='w','b'
for move in moves:
    piece=move[0:2]
    if turn=='w':
        print('white move:',move)
    else:
        print('black move:',move)
    if move[0] != turn:
        print('error',move)
        exit()
    if validposition(move)==False:
        print('error',move)
        exit()
    sc,sr=ldict[move[3]],ndict[move[5]]
    ec,er=ldict[move[8]],ndict[move[10]]
    if chess[sr][sc]!=move[0:2] or not(validposition(move)) or validmove(move)==True:
        print('error',move)
        exit()
    if valid1move(chess,piece,sr,sc,er,ec) == True:
        chess[er][ec]=piece
        chess[sr][sc]='--'
    else:
        print('error',move)
        exit()
    if checkmate(chess,rturn,turn) == True:
        printboard(chess)
        if turn=='w':
            print('white win!')
        else:
            print('black win!')
        exit()
    if turn=='w':
        turn='b'
        rturn='w'
    else:
        turn='w'
        rturn='b'
    #check if own move result king in check
    if turn=='w' and rturn=='b':
        if kingcheck(chess,'b')==True:
            print('error',move)
            exit()
    else:
        if kingcheck(chess,'w')==True:
            print('error',move)
            exit()
    printboard(chess)
