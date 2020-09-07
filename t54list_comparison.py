

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
# x=[2,3]              
# y=[2,3,2,3]    
y="dogcatwhattac"
x="cat"

# def myreverse(p):
#     i=0
#     mid=len(p)/2
#     high=len(p)
#     while i<mid:
#         a=p[i]
#         p[i]=p[high-1]
#         p[high-1]=a
#         i=i+1
#         high=high-1

def myreverse_string(p):
    high=len(p)
    i=high-1
    low=0
    p2=""
    while i>=low:
        p2=p2+p[i]
        i=i-1
    return p2







def count_sublists(p,p2):
    pl=len(p)
    i=0
    i2=0
    good=0
    while i<pl-1:
        low=i
        if i+len(p2)<=pl:
            high=i+len(p2)
        else:
            break
        # t=[]
        # for i2 in range(low,high,1):
        #     t.append(p[i2])
        t=p[low:high]
        print(t)
        if t==p2:
            good +=1
            print(t,p2)
        else:
            res=myreverse_string(t)
            print(res)
            # t.reverse()
            if res==p2:
                good +=1
                print(t,p2)

            
        i +=1
    print(good)
            

count_sublists(y,x)

# print(myreverse_string(y))