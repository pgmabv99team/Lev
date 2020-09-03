

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
y=[2,4,5,2,3,2]           
def extract_sublists(p,k,p2):
    pl=len(p)
    i=0
    i2=0
    while i<pl-1:
        low=i
        if i+k<pl:
            high=i+k
        else:
            break
        t=[]
        for i2 in range(low,high,1):
            t.append(p[i2])

        print(t)
        i +=1
extract_sublists(y,3,x)
        