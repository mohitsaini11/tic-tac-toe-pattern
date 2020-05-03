import random
from tictactoe2 import *
help_computer=[11,12,13,21,22,23,31,32,33]
user_list = []
computer_list=[]
combined=[]
def diffpat(s,userk,computerk):
    for m in range(0,len(userk)):
        if userk[m]==s:
            print('X',end='')
            break
    else:
        for l in range(0,len(computerk)):
            if computerk[l]==s:
                print('O',end='')
                break

def pattern2(k):
    for i in range(1, 4):
        h = i
        for j in range(7):
            if j % 2 == 0:
                print('|', end='')
            else:
                myno = (j + 1) / 2
                sum1 = h * 10 + myno
                for i in range(len(k)):
                    if k[i] == sum1:
                        diffpat(k[i],user_list,computer_list)
                        break
                else:
                    print(' ', end='')
        print()
    print('-------')
superno=0


#inserting values no starts from here

while True:

    i=1
    user = int(input('enter the coordinate'))# entering the first coordinate
    if i==1:
        user_list.append(user)
        combined.append(user)
        help_computer.remove(user)
    pattern2(combined)
    if len(combined)<9:
        computerno=random.randint(0,len(help_computer)-1)
        computerno2=help_computer[computerno]
        help_computer.remove((computerno2))
        computer_list.append(computerno2)
        combined.append(computerno2)
        pattern2(combined)
    i+=1
    if len(user_list)>=3:
        hope2=hope(user_list)
        if hope2==1:
            print('user has won!!!!1')
            break
    if len(computer_list)>=3:
        hope2=hope(computer_list)
        if hope2==1:
            print('computer has won!!')
            break


    if len(combined)==9:
        print('it is a draw')
        break














