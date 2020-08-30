import math
import random
def prime(p):
    pl=len(p)
    i=0
    i2=0
    bad=0
    while i<pl:
        while True:
            if i2!=0:
                if p[i2]%i2!=0:
                    i2=i2+1
                    if i2==p[i]:
                        break
                    continue
                else:
                    bad=bad+1
                    continue
            else:
                i2 +=1
                continue
        i +=1
    if bad>0:
        print("bad array")
    else:
        print("good array")
x=[17,18]
# prime(x)

def prime2(p):
    i=2
    bad=0
    good=0
    divide=0
    while i<p:
        if p%i==0:
            bad +=1
        elif p%i!=0 and i*2<p:
            good +=1
        divide +=1
        i +=1
    if bad>0:
        print("Not Prime")
    else:
        print("Prime")
    print("Divided ",divide,"times")
# prime2(37)

# def mysqrt(p):
#     i=0

#     while i<p:
#         if i*i==p:
#             print("sqrt of",p,"is",i)
#             break
#         elif i*i>p:
#             print("The sqrt is between",i-1,"and",i)
#             break
#         else:
#             i +=1

def mysqrt2(p):
    low=0
    if p>=1:
        high=p/2
    else:
        high=p
    for i in range(16):
        mid=(low+high)/2
        if mid**2>p:
            print("sqrt between",low,"and",mid)
            high=mid

        else:
            print("sqrt between",mid,"and",high)
            low=mid
    return low
num=6
# mysqrt2(27)
def make_random(p):
    i=0
    while i<num:
        p.append(random.randint(0,100))
        i +=1
    
x=[]
make_random(x)

i=0
xl=len(x)
q=[]
while i<xl:
    res=mysqrt2(x[i])
    q.append(res)
    i +=1
print(x)
print(q)

def turn_around(p):
    print(p)
    i=0
    pl=len(p)
    pl2=len(p)
    while i<pl/2:
        a=p[i]
        p[i]=p[pl-i-1]
        p[pl-i-1]=a
        i +=1
        
    print(p)


turn_around(x)
turn_around(q)