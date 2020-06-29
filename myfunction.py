# implementing functions
def MyFunction(p):
    pl = len(p)
    i = 0
    sum = 0
    nneg = 0
    # find the first positive
    j = 0
    while j < pl:
        if p[j] < 0:
            break
        j = j+1
    if j < pl:
        mymax = p[j]
    else:
        mymax = "no luck......try again?"

    # main loop
    while i < pl:
        if p[i] < 0:
            # working on sum
            sum = sum+p[i]
            nneg += 1
            # working on min
            if p[i] > mymax:
                mymax = p[i]
        i = i+1

    if nneg > 0:
        ave = sum/nneg
    else:
        ave = "|-|OLY SHIT THIS TOOK A LONG TIME"
    return ave,mymax
    



