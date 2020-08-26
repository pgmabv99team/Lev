x=[1,2,3,4,5]
def backward(p):
    i=0
    pl=len(p)/2
    pl2=len(p)
    while i<pl:
        a=p[i]
        p[i]=p[pl2-1]
        p[pl2-1]=a
        i=i+1
        pl2=pl2-1
    print(p)
# backward(x)

def shift(p):
    i=1
    pl=len(p)
    a=p[0]
    while i<pl:
        print(i-1)
        p[i-1]=p[i]
        i=i+1
    p[pl-1]=a
    print(p)
shift(x)

    



