# slow function 
def triplets(p):
    pl=len(p)
    mymax=p[0]*p[1]*p[2]
    for i1 in range(pl):
        for i2 in range(pl):
            if i2==i1:
                continue
            for i3 in range(pl):
                
                if i1==i3 or i2==i3  :
                    i3 +=1
                    continue
                trip=p[i1]*p[i2]*p[i3]
                
                if trip>mymax:
                    mymax=trip
    
    return mymax

# print(triplets([2,2,2,23]))
def maxpop(p):
    pl=len(p)
    mymax=p[0]
    imax=0
    for i in range(pl):
        if p[i]>mymax:
            mymax=p[i]
            imax=i      
    p.pop(imax)  
    return mymax      

def minpop(p):
    pl=len(p)
    mymin=p[0]
    imin=0
    for i in range(pl):
        if p[i]<mymin:
            mymin=p[i]
            imin=i

   
    p.pop(imin)
    return mymin
# fast function
def triplets2(p):
    t=p.copy()
    pl=len(p)
    i=0
    neg=0
    pos=0
    while i<pl:
        if p[i]<0:
            neg +=1
        elif p[i]>=0:
            pos +=1
        i +=1
    
    
    if neg==pl or pos==pl:
        a1=maxpop(p)
        a2=maxpop(p)
        a3=maxpop(p)
        print("3 maxpops",a1,a2,a3)
        return a1*a2*a3
    elif neg==1:
        a1=maxpop(p)
        a2=maxpop(p)
        a3=maxpop(p)
        print("3 maxpops",a1,a2,a3)
        return a1*a2*a3
    elif neg>=2 and pos==1:
        a1=maxpop(p)
        b1=minpop(p)
        b2=minpop(p)
        print("1 maxpop and 2 minpops",a1,b1,b2)
        return a1*b1*b2
    elif neg>=2 and pos>1:
        t=p.copy()
        a1=maxpop(p)
        b1=minpop(p)
        b2=minpop(p)
        

        a2=maxpop(t)
        a3=maxpop(t)
        a4=maxpop(t)
        if a1*b1*b2>a2*a3*a4:
            print("maxpop and 2 minpop",a1,b1,b2)
            return a1*b1*b2
        else:
            print("3 maxpops",a2,a3,a4)
            return a2*a3*a4


# print(triplets2([1,2,3,-1,-5]))
# print(triplets2([1,20,30,-1,-5]))
# print(triplets2([1,20,30,5,2]))
# print(triplets2([-5,-4,-3,-5]))
# print(triplets2([4,3,2,0]))
from random import seed
from random import randint

n=10**6
d=[0]*n
seed(1)
for i in range(n):
    d[i]=randint(-n,n)




# timing the function
import time
start_time = time.time()
print(triplets2(d))
print("--- %s seconds ---" % (time.time() - start_time))
