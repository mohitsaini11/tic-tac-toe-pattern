import random
from tictactoe2last  import *
help_computer=[11,12,13,21,22,23,31,32,33]
user_list = []
computer_list=[]
combined=[]
computertoss=random.randint(0,1)


def diffpat(s,userk,computerk,final):
    global enter
    global player2sign
    for m in range(0,len(userk)):
        if userk[m]==s:
            print(enter,end='')
            break
    else:
        for l in range(0,len(computerk)):
            if computerk[l]==s:
                if final=='computer':
                    print('O',end='')
                    break
                elif final=='player2':
                    print(player2sign,end='')
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
                        diffpat(k[i],user_list,computer_list,player2)
                        break
                else:
                    print(' ', end='')
        print()
    print('-------')
superno=0
enter = input('enter your sign of identification')
user_name=input('enter your name')
player2=input('do you want to play with computer or player2')
if player2=='player2':
    player2_name=input('enter player2 name.')
    player2sign=input('enter your sign of identification')
ask=int(input('press 0 for tail and 1 for head'))
com=0
if ask==computertoss:
    print(user_name,' has won the toss!!')
    com=com+1
elif ask!=computertoss:
    if player2=='computer':
        print('computer won the toss')
    elif player2=='player2':
        print(player2_name,'hasd won the toss')
    com=com+2
else:
    print('something went wrong!!!')


while True:

    if com==1:
        user = int(input('enter the coordinate'))
        user_list.append(user)
        combined.append(user)
        help_computer.remove(user)
        pattern2(combined)
    if len(user_list)>=3:
        hope2=hope(user_list)
        if hope2==1:
            print(user_name,'has won!!!!1')
            break

    if player2=='computer':
        if len(combined)<9:
            computerno=random.randint(0,len(help_computer)-1)
            computerno2=help_computer[computerno]
            help_computer.remove((computerno2))
            computer_list.append(computerno2)
            combined.append(computerno2)
            pattern2(combined)
    elif player2=='player2':
        player2k=int(input('enter your coordinate'))
        computer_list.append(player2k)
        combined.append(player2k)
        pattern2(combined)


    if len(computer_list)>=3:
        hope2=hope(computer_list)
        if hope2==1:
            if player2=='player2':
                print(player2_name ,'has won!!')
                break
            else:
                print('computer has won!!')
                break

    if len(combined) == 9:
        print('it is a draw')
        break
    com=1














