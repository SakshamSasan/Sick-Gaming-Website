import random

def turn():
    
    choice=input("Please select 'r', 'p' or 's': ")
    comp=random.choice(['r','p','s'])
    
    if comp==choice:
        return 0
    else :
        if comp=='r' and choice=='p':
            return 1
        if comp=='p' and choice=='s':
            return 1
        if comp=='s' and choice=='r':
            return 1
    return -1



plays=5
n=0
compsc=0
playersc=0
while n<plays:
    
    result=turn()
    if result==0:
        pass
    elif result==1:
        playersc+=1
    else:
        compsc+=1
    
    n+=1
if compsc==playersc:
    print("It's a tie!")
elif compsc>playersc:
    print("Sadly, the computer has won!")
else:
    print("Congrats! You have won the game.")