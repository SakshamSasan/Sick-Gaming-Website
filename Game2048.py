
import random

def start():
    arr=[[0 for j in range(4)] for i in range(4)]
    return arr

def add_2(arr):
    row=random.randint(0,3)
    col=random.randint(0,3)
    while arr[row][col]!=0:
        row=random.randint(0,3)
        col=random.randint(0,3)
        
    arr[row][col]=2

def get_state(arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j]==2048:
                return 'Won'
            
    #Anywhere 0 is present
    for i in range(4):
        for j in range(4):
            if arr[i][j]==0:
                return 'In Progress'
            
    #Additions can be done even if 0 not there
    for i in range(3):
        for j in range(3):
            if (arr[i][j]==arr[i+1][j] or arr[i][j]==arr[i][j+1]):
                return 'In Progress'
    
    #For Last Row and Column
    for j in range(3):
        if arr[3][j]==arr[3][j+1]:
            return 'In Progress'
    
    for i in range(3):
        if arr[i][3]==arr[i+1][3]:
            return 'In Progress'
    
    return 'Lost'

def compress(arr):
    change=False
    new_arr=[[0 for j in range(4)] for i in range(4)]
    
    for i in range(4):
        pos=0
        for j in range(4):
            if arr[i][j]!=0:
                new_arr[i][pos]=arr[i][j]
                if j!=pos:
                    change=True
                pos+=1
    
    return new_arr,change

def merge(arr):
    change=False
    for i in range(4):
        for j in range(3):
            if arr[i][j]==arr[i][j+1] and arr[i][j]!=0:
                arr[i][j]*=2
                arr[i][j+1]=0
                change=True
            
    return arr,change
            
def reverse(arr):
    new_arr=[]
    for i in range(4):
        new_arr.append([])
        for j in range(4):
            new_arr[i].append(arr[i][4-j-1])
    
    return new_arr

def transpose(arr):
    new_arr=[]
    for i in range(4):
        new_arr.append([])
        for j in range(4):
            new_arr[i].append(arr[j][i])
    
    return new_arr
    
def move_left(grid):
    
    new_grid,changed1=compress(grid)
    new_grid,changed2=merge(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress(new_grid)
    return new_grid,changed

def move_right(grid):
    reversed_grid=reverse(grid)
    new_grid,changed1=compress(reversed_grid)
    new_grid,changed2=merge(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress(new_grid)
    final_grid=reverse(new_grid)
    return final_grid,changed

def move_up(grid):
    transposed_grid=transpose(grid)
    new_grid,changed1=compress(transposed_grid)
    new_grid,changed2=merge(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress(new_grid)
    final_grid=transpose(new_grid)
    return final_grid,changed

def move_down(grid):
    transposed_grid=transpose(grid)
    reversed_grid=reverse(transposed_grid)
    new_grid,changed1=compress(reversed_grid)
    new_grid,changed2=merge(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress(new_grid)
    final_reversed_grid=reverse(new_grid)
    final_grid=transpose(final_reversed_grid)
    return final_grid,changed
    
    

