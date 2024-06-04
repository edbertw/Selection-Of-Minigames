mapfile=int(input("Choose a map (0-4): "))
templist=[]
linelist=[]
with open(f"{mapfile}.map") as file:
    for line in file:
        for i in line:
            templist=templist+[i]
        linelist.append(templist)
        templist=[]
def printmap():
    for i in range(len(linelist)):
        for j in range(len(linelist[i])):
            print(linelist[i][j],end="")
for i in range(len(linelist)):
    for j in range(len(linelist[i])):
        if linelist[i][j]=='P':
            hori=i
            verti=j
            break
def validatemove(move):
    if move=='w':
        if linelist[hori-1][verti]=='X':
            return False
    elif move=='a':
        if linelist[hori][verti-1]=='X':
            return False
    elif move=='s':
        if linelist[hori+1][verti]=='X':
            return False
    elif move=='d':
        if linelist[hori][verti+1]=='X':
            return False
    return True
bool1=False
def makemove(move):
    global linelist,hori,verti,bool1
    if move=='w':
        if linelist[hori][verti]=='P' and linelist[hori-1][verti]=='0':
            bool1=True
            linelist[hori-1][verti]='P'
            linelist[hori][verti]=' '
            hori=hori-1
            return True
        if linelist[hori][verti]=='P' and linelist[hori-1][verti]=='&' and linelist[hori-2][verti]=='0':
            linelist[hori-1][verti]='P'
            linelist[hori][verti]=' '
            linelist[hori-2][verti]=' '
            if bool1==True:
                bool1=False
                linelist[hori][verti]='0'
            hori=hori-1
            return True
        if linelist[hori-1][verti]=='&':
            if linelist[hori-2][verti]=='X' or linelist[hori-2][verti]=='&':
                return False
            else:
                linelist[hori-2][verti]='&'
                linelist[hori-1][verti]='P'
                linelist[hori][verti]=' '
                if bool1==True:
                    bool1=False
                    linelist[hori][verti]='0'
                hori=hori-1
        else:
            linelist[hori-1][verti]=linelist[hori][verti]
            linelist[hori][verti]=' '
            if bool1==True:
                bool1=False
                linelist[hori][verti]='0'
            hori=hori-1
    elif move=='a':
        if linelist[hori][verti]=='P' and linelist[hori][verti-1]=='&' and linelist[hori][verti-2]=='&':
            return False
        if linelist[hori][verti]=='P' and linelist[hori][verti-1]=='0':
            bool1=True
            linelist[hori][verti-1]='P'
            linelist[hori][verti]=' '
            verti=verti-1
            return True
        if linelist[hori][verti]=='P' and linelist[hori][verti-1]=='&' and linelist[hori][verti-2]=='0':
            linelist[hori][verti]=' '
            linelist[hori][verti-1]='P'
            linelist[hori][verti-2]=' '
            if bool1==True:
                bool1=False
                linelist[hori][verti]='0'
            verti=verti-1
            return True
        if linelist[hori][verti-1]=='&':
            if linelist[hori][verti-2]=='X':
                return False
            else:
                linelist[hori][verti-2]='&'
                linelist[hori][verti-1]='P'
                linelist[hori][verti]=' '
                if bool1==True:
                    bool1=False
                    linelist[hori][verti]='0'
                verti=verti-1
        else:
            linelist[hori][verti-1]=linelist[hori][verti]
            linelist[hori][verti]=' '
            if bool1==True:
                bool1=False
                linelist[hori][verti]='0'
            verti=verti-1
    elif move=='s':
        if linelist[hori][verti]=='P' and linelist[hori+1][verti]=='0':
            bool1=True
            linelist[hori+1][verti]='P'
            linelist[hori][verti]=' '
            hori=hori+1
            return True
        if linelist[hori][verti]=='P' and linelist[hori+1][verti]=='&' and linelist[hori+2][verti]=='0':
            linelist[hori][verti]=' '
            linelist[hori+1][verti]='P'
            linelist[hori+2][verti]=' '
            hori=hori+1
            if bool1==True:
                bool1=False
                linelist[hori][verti]='0'
            return True
        if linelist[hori+1][verti]=='&':
            if linelist[hori+2][verti]=='X' or linelist[hori+2][verti]=='&':
                return False
            else:
                linelist[hori+2][verti]='&'
                linelist[hori+1][verti]='P'
                linelist[hori][verti]=' '
                if bool1==True:
                    bool1=False
                    linelist[hori][verti]='0'
                hori=hori+1
        else:
            linelist[hori+1][verti]=linelist[hori][verti]
            linelist[hori][verti]=' '
            if bool1==True:
                bool1=False
                linelist[hori][verti]='0'
            hori=hori+1
    elif move=='d':
        if linelist[hori][verti]=='P' and linelist[hori][verti+1]=='&'and linelist[hori][verti+2]=='&':
            return False
        if linelist[hori][verti]=='P' and linelist[hori][verti+1]=='0':
            bool1=True
            linelist[hori][verti+1]='P'
            linelist[hori][verti]=' '
            verti=verti+1
            return True
        if linelist[hori][verti]=='P' and linelist[hori][verti+1]=='&' and linelist[hori][verti+2]=='0':
            linelist[hori][verti]=' '
            linelist[hori][verti+1]='P'
            linelist[hori][verti+2]=' '
            if bool1==True:
                bool1=False
                linelist[hori][verti]='0'
            verti+=1
            return True
        if linelist[hori][verti+1]=='&':
            if linelist[hori][verti+2]=='X':
                return False
            else:
                linelist[hori][verti+2]='&'
                linelist[hori][verti+1]='P'
                linelist[hori][verti]=' '
                if bool1==True:
                    bool1=False
                    linelist[hori][verti]='0'
                verti=verti+1
        else:
            linelist[hori][verti+1]=linelist[hori][verti]
            linelist[hori][verti]=' '
            if bool1==True:
                bool1=False
                linelist[hori][verti]='0'
            verti=verti+1
    return True
def checkwin():
    for i in range(len(linelist)):
        for j in range(len(linelist[i])):
            if linelist[i][j]=='0':
                return False
    return True
printmap()
while True:
    move=input("Your Move [wasdq]: ")
    if move=="w":print("Making Move: N")
    elif move=='a':print("Making Move: W")
    elif move=='s':print("Making Move: S")
    elif move=='d':print("Making Move: E")
    elif move=='q':
        print("BYE for now ...")
        exit()
    while validatemove(move)==False:
        printmap()
        move=input("Your Move [wasdq]: ")
        if move=="w":print("Making Move: N")
        elif move=='a':print("Making Move: W")
        elif move=='s':print("Making Move: S")
        elif move=='d':print("Making Move: E")
        elif move=='q':
            print("BYE for now ...")
            exit()
    while makemove(move)==False:
        printmap()
        move=input("Your Move [wasdq]: ")
        if move=="w":print("Making Move: N")
        elif move=='a':print("Making Move: W")
        elif move=='s':print("Making Move: S")
        elif move=='d':print("Making Move: E")
        elif move=='q':
            print("BYE for now ...")
            exit()
    printmap()
    if checkwin()==True:
        break
print('You WIN!')
