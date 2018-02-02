
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

# The first Queen is set at column 0 and row 0, and it is safe, therefore we start the search for new safe spot in the column 1

def solve(size): 
    n = 0
    solution = 0
    while True :
        if n == -1:
            break
        elif n == size:
            solution += 1
            print("solution number " + str(solution))
            printBoard(size)
            queen[n-1] = queen[n-1] +1
            n-=1
        elif queen[n] == size:
            queen[n] =0
            queen[n-1] = queen[n-1] +1
            n-=1
        elif isSafe(n) == False:
            queen[n] = queen[n] +1
        elif isSafe(n) == True:
            n += 1
        




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
        p -= 1
        diagUp -= 1
        diagDown += 1
    
    #Once the row and diagonal checks are complete, the row n is safe, return True
    return True 

def printBoard(size):
    #create a blank board
    board = []
    for rows in range(0, size):
        board.append([])
        for cols in range(0, size):
            board[rows].append([])
            board[rows][cols] = 0

    #set each occupied spot with 1, each column by column
    for setCol in range(0, size):
        board[queen[setCol]] [setCol] = 1
    
    #print the board, row by row
    for printRow in range(0, size):
        print(board[printRow])

solve(size)