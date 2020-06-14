import random
def good(x):
    for i in range(x):        # x will decide how many random yet to be choosen!
        s=random.randint(1,len(m))
        for o in range(len(ralist)):
            if s==ralist[o]:
                break
        else:
            ralist.append(s)
fvar=0
ralist=[]
imp=[]
value2=1
n=input('enter the value')
m=str(n)
for i in range(1,len(m)+1):  # doing factorial for getting the no of the permutations available
    value2=value2*i
def last(ni):
    global fvar
    global finebro
    for i in range(ni):
        xp=len(m)
        good(xp)
        while True:
            bouncer=len(m)-len(ralist)
            if bouncer>0:
                good(bouncer)
            elif bouncer==0:
                break
        sum=0
        for j in range(len(m)):
            ten=10**j
            final=ralist[j]*ten
            sum=sum+final
        if finebro==0:
            if i==0:       ## har bar zero hi milagi
                imp.append(sum)
            else:
                for mohit in range(len(imp)):   #checking duplicacy here
                    if sum==imp[mohit]:
                        fvar+=1
                        break
                else:
                    imp.append(sum)
        else:
            for mohit in range(len(imp)):  # checking duplicacy here
                if sum == imp[mohit]:
                    fvar += 1
                    break
            else:
                imp.append(sum)

        ralist.clear()

# calling work starts from here
finebro=0
last(value2)
while True:
    aman=value2-len(imp)
    if aman>0:
        finebro+=1
        last(aman)
    elif aman==0:
        break

h=0
print('last',imp)
for i in range(len(imp)):
    for j in range(1,len(imp)):
        if imp[i]==imp[j]:
            h+=1
            if i==j:
                h=h-1
print('duplicate values',h/2)
print('the required no is ',value2,'obtained no is ',len(imp))
print('permutations start from here')
testing=[]
mainlist=[]
p=''
for g in range(len(m)):
    a=m[g:g+1]
    testing.append(a)
for i in range(len(imp)):
    a=imp[i]
    while a>0:
        remainder=a%10
        p=p+testing[remainder-1]
        #print(testing[remainder-1],end='')
        a=a//10
    mainlist.append(p)
    p=''

print(mainlist)
print('PERMUTUATE','INDEX')
for i in range(len(mainlist)):
    print(mainlist[i],'    index=',i)

search=input('enter the search value')
for i in range(len(mainlist)):
    if search==mainlist[i]:
        print('found at index =',i)
        break
else:
    print('error!!!')
