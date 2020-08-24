x=[3,3,1]
def is_up(p):
    pl=len(p)
    i=0
    u=0
    d=0
    while i<pl-1:
        if p[i]>p[i+1]:
            print("Down")
            d=d+1
        elif p[i]<p[i+1]:
            print("Up")
            u=u+1
        else:
            print("No Move")
        i=i+1
    if d>0 and u==0:
        print("Good Array")
    elif d==0 and u>0:
        print("Good Array")
    else:
        print("Bad Array")
is_up(x)
