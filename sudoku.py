from dokusan import generators
import numpy as np
import copy
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
def isSafe(board,i,j,number):
    for column in range(0,9):
        if board[i][column]==number:
            return False
    for row in range(0,9):
        if board[row][j]==number:
            return False
    
    if i>=0 and i<=2:
        ur=2
        lr=0
    elif i>=3 and i<=5:
        ur=5
        lr=3
    else:
        ur=8
        lr=6
    if j>=0 and j<=2:
        uc=2
        lc=0
    elif j>=3 and j<=5:
        uc=5
        lc=3
    else:
        uc=8
        lc=6
    for row in range(lr,ur+1):
        for column in range(lc,uc+1):
            if board[row][column]==number:
                return False
    
    return True

def solve_sudoku(board,i=0,j=0):
    if i>=9:
        return True
    
    if board[i][j]!=0:
        if j==8:
            return solve_sudoku(board,i+1,0)
        else:
            return solve_sudoku(board,i,j+1)
    
    for number in range(1,10):
        if isSafe(board,i,j,number):
            board[i][j]=number
            if j==8:
                ans =solve_sudoku(board,i+1,0)
            else:
                ans= solve_sudoku(board,i,j+1)
            if ans is True:
                return True
            board[i][j]=0
        
    return False





def printarr(li):
    for i in range(len(li)):
        for j in range(len(li[i])):
            print(li[i][j],end=" ")
        print()



#Generating a sudoku puzzle with rank = 150
arr=np.array(list(str(generators.random_sudoku(avg_rank=150))))
arr=arr.reshape(9,9)
arr=arr.tolist()
#arr=[[8,9,0,0,0,4,0,0,0],[0,6,0,0,1,0,0,0,5],[0,0,2,3,0,0,0,0,0],[0,2,3,9,0,0,0,0,0],[9,0,4,0,0,7,0,0,0],[5,7,6,2,4,0,0,8,0],[2,0,0,0,0,0,7,0,4],[6,5,1,0,0,0,0,0,8],[0,0,0,0,0,8,0,2,1]]
input_array=copy.deepcopy(arr)
printarr(input_array)
print()
#collecting user's array in variable called user
print("Please fill in the 0s and give your input")
user=[]
for i in range(9):
    arr=input().split()
    for j in range(len(arr)):
        arr[j]=int(arr[j])
    user.append(arr)

solution=solve_sudoku(input_array)
if solution==False:
    print("No solution exists to this puzzle")
else:
    print()
    if (user==input_array):
        print("Congrats! Wanna play again?")
    else:
        print("Wrong answer! Please try again")



