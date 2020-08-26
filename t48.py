x=[1,2,3,4,5]
def shift_right(p):
    pl=len(p)
    i=pl-1
    a=x[pl-1]
    while i>=1:
        x[i]=x[i-1]
        i=i-1
    x[0]=a
    print(p)

    
shift_right(x)
