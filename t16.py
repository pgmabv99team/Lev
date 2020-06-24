x = [2,3,45,4]
xl = len(x)


def Iteration():
    i = 0
    naction = 0
    while i < xl-1:
        #print(x[i], x[i+1])
        if x[i] > x[i+1]:
            #print("Swapping", x[i], x[i+1])
            h = x[i]
            x[i] = x[i+1]
            x[i+1] = h
            naction = naction+1

        i = i+1
    return naction

naction=1
j = 0
while naction>0:
    print("before iteration", x, j)
    naction = Iteration()
    print("action", naction)
    print("after iteration", x, j)
    if naction == 0:
        break

    j = j+1
