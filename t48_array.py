x=[1,2,3,4,5]
# def shift_right(p):
#     pl=len(p)
#     i=pl-1
#     a=x[pl-1]
#     while i>=1:
#         x[i]=x[i-1]
#         i=i-1
#     x[0]=a
#     print(p)

def xsum(p):
    pl=len(p)
    i=pl-1
    mysum=0
    mymax=None
    while i>=0:
        if i%2==1:
            # if mymax==None or p[i]>mymax:
            #     mymax=p[i]
            if mymax==None:
                mymax=p[i]
            else:
                if p[i]>mymax:
                    mymax=p[i]
            mysum=mysum+p[i]
        i=i-1
    print(mysum)
    print(mymax)

    
# xsum(x)

def check_gap(p):
    pl=len(p)
    i=pl-1
    good=0
    bad=0
    while i>=1:
        print(p[i],p[i-1])
        if p[i]-p[i-1]>2:
            bad +=1
        else:
            good +=1
        i=i-1
    if bad>0:
        print("Bad Loop")
    else:
        print("Good loop")
check_gap([1,2,3])