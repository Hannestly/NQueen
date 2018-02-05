import time
size = input("Enter the number of Queen")
size = int(size)
print("The size of the board: " + str(size))
print("The number of Queen you're placing "+ str(size))
unused = []
for i in range(0,size):
    unused.append([])
    unused[i] = i

def perm(lst):
    #the length of the sublist is 0, send an empty array back to add,
    #if size lenghth is 1, send that last, one item back as a list
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        #this list is a list of list, that will contain all the permutation
        l = []
        #we are going to through all the possible digit 
        for i in range(len(lst)):
            #This value will be taken out of the list
            x = lst[i]
            #this is a copy of the list 'without' the value taken out
            xs = lst[:i]+ lst[i+1:]
            #recursion with the list without he value
            for p in perm(xs):
                #since all the values return a list of one item, or empty,
                #we add them to the list one by one
                l.append([x] +p)
        #return the list of lists   
        return l 

def isSafe(posSol):
    #check diagonal values

    for col in range(0,len(posSol)-1):
        diagUp = posSol[col] -1
        for checkUp in range(col+1,len(posSol)):
            if posSol[checkUp] == diagUp:
                return False
            else:
                diagUp -=1
        diagDown = posSol[col] +1
        for checkDown in range(col+1,len(posSol)):
            if posSol[checkDown] == diagDown:
                return False
            else:
                diagDown += 1
    return True

def printBoard(p):
    size = len(p)
    #create a blank board
    board = []
    for rows in range(0, size):
        board.append([])
        for cols in range(0, size):
            board[rows].append([])
            board[rows][cols] = 0

    #set each occupied spot with 1, each column by column
    for setCol in range(0, size):
        board[p[setCol]] [setCol] = 1
    
    #print the board, row by row
    for printRow in range(0, size):
        print(board[printRow])



t0 = time.time()
for p in perm(unused):
    if isSafe(p) == True:
        print("solution found")
        printBoard(p)
        break
t1 = time.time()
print(t1-t0)