def myskip(p):
    pl=len(p)
    i=0
    p.sort()
    if pl==0:
        return 1
    if p[0]!=1 :
        return 1
    elif p[pl-1]!=pl+1:
        return pl+1
    while i<pl:
        if p[i]+1==p[i+1]:
            i +=1
            # good pair/ no gap
            continue
        else:
            return p[i+1]-1
x=[]       
print(myskip(x))
