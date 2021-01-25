def bcomp(a,b):
    if abs(a)>abs(b):
        return True
    return False

def bcomp_abs(a):
    return abs(a)


def bcomp2(a,b):
    if len(a)>len(b):
        return True
    return False




def bsort(p,myfunc):
    pl=len(p)
    i=0
    while i<pl-1:
        if myfunc(p[i],p[i+1]):
            a=p[i]
            p[i]=p[i+1]
            p[i+1]=a
            i=0
            continue
        i +=1
    return p
# print(bsort([4,3,2,1]))
# print(bsort([5,6,3,6,2]))
# print(bsort([0,1,4,3]))
# print(bsort(["aaa","cr","d","b"],bcomp))
# print(bsort(["aaa","cr","d","b"],bcomp2))

from random import seed
from random import randint

n=10**3
d=[0]*n
seed(1)
for i in range(n):
    d[i]=randint(-n,n)
import time
t1=time.time()
bsort(d,bcomp)
# d=[-3,4,2,6]
d1=sorted(d)
t2=time.time()
print(t2-t1)