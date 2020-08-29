import math
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

def mysqrt(p):
    i=0

    while i<p:
        if i*i==p:
            print("sqrt of",p,"is",i)
            break
        elif i*i>p:
            print("The sqrt is between",i-1,"and",i)
            break
        else:
            i +=1

def sqrt_range(p):
    i=0

    while i<p:
        if i*i>p:
            
            break
        i +=1
    return i-1,i
p=10
res=sqrt_range(p)
low=res[0]
high=res[1]
for i in range(16):
    mid=(low+high)/2
    if mid**2>p:
        print("sqrt between",low,"and",mid)
        high=mid

    else:
        print("sqrt between",mid,"and",high)
        low=mid
print(math.sqrt(p))


