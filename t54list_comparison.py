

def compare(p,k):
    pl=len(p)
    kl=len(k)
    res=None
    ratio=None
    if kl!=pl:
        res=False
        ratio=None
    else:
        i=0
        good=0
        bad=0
        while i<pl:
            if p[i]==k[i]:
                good +=1
            else:
                bad +=1
            i +=1
        if bad>0:
            res=False
        else:
            res=True
        ratio=format(good/pl, '.2f')

    return res,ratio

# res=compare(x,y) 

# print(x,y,res)
x=[2,3]              
y=[2,3,2,3]    

def reverse(p):
    i=0
    mid=len(p)/2
    high=len(p)
    while i<mid:
        a=p[i]
        p[i]=p[high-1]
        p[high-1]=a
        i=i+1
        high=high-1






def count_sublists(p,k,p2):
    pl=len(p)
    i=0
    i2=0
    good=0
    while i<pl-1:
        low=i
        if i+k<=pl:
            high=i+k
        else:
            break
        t=[]
        for i2 in range(low,high,1):
            t.append(p[i2])
        print(t)
        if t==p2:
            good +=1
            print(t,p2)
        else:
            reverse(t)
            if t==p2:
                good +=1
                print(t,p2)

            
        i +=1
    print(good)
            

count_sublists(y,len(x),x)
        