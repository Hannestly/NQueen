#The user inputs the dimension of the board. The dimension is equal to the number of queens placed 
size = input("Enter the number of Queen")
size = int(size)
print("The size of the board: " + str(size))
print("The number of Queen you're placing "+ str(size))

#1D array is created based on the size input. The address of the array represent the column, and the element represesnt the row of that column
#The initial position of the queens per each column are set at row 0
queen = []
for i in range(0,size):
    queen.append([])
    queen[i] = 0

#The first Queen is set at column 0 and row 0, and it is safe, therefore we start the search for new safe spot in the column 1
n = 0
solution = 0

def solve(n,solution): 
#The base case: ran out of solutions, end the recursion method
    if n == -1:
        return True

#The base case: a solution has been found
    if n == size:
        solution += 1
        print("Solution number " + str(solution))
        printBoard(size)
        queen[n-1] = queen[n-1] + 1
        return solve(n-1,solution)

#executed if the queen cannot find a safe row in a column 
#brings the row value of the column to be 0 (resetting) and calls recursive call of a column before
    if queen[n] == size:
        queen[n] = 0
        queen[n-1] = queen[n-1] +1
        return solve(n-1,solution)
    
    #if the place of current row is safe for the queen of column 'n', then call the recursive call for the next column
    #if the row is not safe, move the row down, and call the function again to check if the new row is safe
    if isSafe(n) == True:
        return solve(n+1,solution)
    else: 
        queen[n] = queen[n]+1
        return solve(n,solution)

def isSafe(n):
    #check if the row is safe
    if n == 0:
        return True

    for rowCheck in range(0, n):
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
    for setCol in range(0,size):
        board[queen[setCol]] [setCol] = 1
    
    #print the board, row by row
    for printRow in range(0,size):
        print(board[printRow])

solve(n,solution)