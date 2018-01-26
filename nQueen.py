size = input("Enter the number of Queen")
size = int(size)
print("The size of the board: " + str(size))
print("The number of Queen you're placing "+ str(size))
queen = []

for i in range(0,size):
    queen.append([])
    queen[i] = 0

n = 1


def solve(n): 
    #The base case: When we are dealing with queen > size of the board, means we have solved the problem
    if n == size:
        printBoard(size)
        return True

    #executed if the queen cannot find a safe row in a column 
    #brings the row value of the column to be 0 (resetting) and calls recursive call of a column before
    if queen[n] == size:
        queen[n] = 0
        queen[n-1] = queen[n-1] +1
        return solve(n-1)
    
    #if the place of current row is safe for the queen of column 'n', then call the recursive call for the next column
    #if the row is not safe, move the row down, and call the function again to check if the new row is safe
    if isSafe(n) == True:
        return solve(n+1)
    else: 
        queen[n] = queen[n]+1
        return solve(n)

def isSafe(n):
    #check if the row is safe
    for rowCheck in range(0, size-1):
        if queen[rowCheck] == queen[n]:
            return False
    
    #Check for diagonal 
    p = n-1
    diagUp = queen[n] - 1 #Checks for diagonal up 
    diagDown = queen[n] + 1 #Check for diagonal down
    while p >= 0:
        if queen[p] == diagUp or queen[p] == diagDown:
            return False
        else: 
            p -= 1
            diagUp -= 1
            diagDown += 1
    
    #Once the row and diagonal checks are complete, the row n is safe, return True
    return True 

def printBoard(size):
    #create a black board
    board = []
    for rows in range(0, size):
        board.append([])
        for cols in range(0, size):
            board[rows].append([])
            board[rows][cols] = 0

    #set each occupied spot with 1, each column by column
    for setCol in range(0,size-1):
        board[queen[setCol]][setCol] == 1
    
    #print the board, row by row
    for printRow in range(0,size-1):
        print("\n"+board[printRow] )
    
solve(n)