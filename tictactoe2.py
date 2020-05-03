positive=[]
def cleaning(kite):
    lotus=0
    for i in range(len(positive)):
        no=positive[i]
        for k in range(len(kite)):
            if kite[k]==no:
                lotus=lotus+1
                break

    return lotus

def hope(clone):
    finaldigit=0
    global lotus
    oil=len(clone)
    for i in range(oil):
        first=clone[i]
        positive.append(first)
        for k in range(i+1,oil):
            second=clone[k]
            positive.append(second)
            for j in range(k+1,oil):
                third=clone[j]
                positive.append(third)
                sum=first+second+third
                if sum == 36 or sum == 96 or sum == 69 or sum == 63:
                    finaldigit=finaldigit+1
                    break
                elif sum == 66:
                    a1 = [12, 21, 33]
                    b1 = [32, 23, 11]
                    check1=cleaning(a1)
                    if check1==3:
                        continue
                    else:
                        check2=cleaning(b1)
                        if check2==3:
                            continue
                        else:
                            finaldigit=finaldigit+1
                            break


                positive.remove(third)
            positive.remove(second)
        positive.remove(first)
    return finaldigit