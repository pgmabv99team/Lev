# Prime or not
def IsPrime(pn):

    i = 2
    flag = True
    while i < pn-1:
        if pn % i == 0:
            print(pn, "/", i, "so... Not Prime")
            flag = False
            # break

        i = i+1
    return flag


print(IsPrime(37969))
