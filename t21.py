

def MyFunction(p):
    pl = len(p)

    sum = 0
    neven = 0
    mymax=None
    # if x[0] % 2 == 0:
    #     mymax = x[0]
    #     mymaxfound = True
    # else:
    #     mymaxfound = False
    # main loop
    i = 0
    while i < pl:
        if p[i] % 2 == 0:
            # working on sum
            sum = sum+p[i]
            neven += 1
            if mymax==None:
                mymax=p[i]
            else:
                if p[i] > mymax:
                    mymax = p[i]

        i = i+1

    if neven > 0:
        ave = sum/neven
    else:
        ave = "|-|OLY SHIT THIS TOOK A LONG TIME"

    return ave, mymax


# Main Function
x = [-3, -1]
y = [233, -4, -45, -7865, 234]
print(x)
res = MyFunction(x)
resave = res[0]
resmax = res[1]
print("for negatives:average=", resave, "maximum=", resmax)
print(y)
res = MyFunction(y)
resave = res[0]
resmax = res[1]
print("for negatives:average=", resave, "maximum=", resmax)
