x=[0,1,2,3]
def perm(p):
    pl=len(p)
    i0=0
    while i0<pl:
        i1=0
        while i1<pl:
            if i0!=i1:
                print(p[i0],p[i1])
            i1 +=1

        i0 +=1


def is_unique(objs):
    x={}
    for obj in objs:
        mykey=obj
        if mykey==None:
            continue
        if mykey in x:
            return False
        else:
            x[mykey]=obj
    return True


x=['a','b','c','d']
def perm2(p,m):
    pl=len(p)
    cnt=0
    ids=[0]*m
    for i0 in range(pl):
        ids[0]=i0
        for i1 in range(pl):
            ids[1]=i1
            for i2 in range(pl):
                ids[2]=i2
                print(ids)
                if is_unique(ids):
                    cnt +=1
                    print(p[i0],p[i1],p[i2])
    print(cnt)

def list_2_string(p):
    x=""
    for i in range(len(p)):
        x=x+str(p[i])
    return x


# permitation with recursion
def perm2_rec(p,m,ids,depth):
    global cnt
    global mydict
    pl=len(p)
    filler="--"*(depth+1)
    for i0 in range(pl):
        ids[depth]=i0
        print(filler,p[i0],"ids",ids)
        if is_unique(ids)==False:
            print(filler,"Early rejection: double found")
            continue
        if depth==m-1:
            # full depth reached
            if is_unique(ids):
                # ids are unique
                cnt +=1
                pids=[]
                for id in ids:
                    pids.append(p[id])
                pids_str=list_2_string(pids)
                pids_sort=sorted(pids)
                pids_sort_str=list_2_string(pids_sort)
                print(filler,"accepted",pids,pids_sort,pids_sort_str)
                #use sorted as key
                #accumulate of unsorted as value
                key=pids_sort_str
                val=pids_str
                if key  not in mydict:
                    mydict[key]=val
                else:
                    mydict[key]=mydict[key]+","+val
            else:
                print(filler,"rejected")              

                
        else:
            # depth not reached. call func again
            perm2_rec(p,m,ids,depth+1)
    ids[depth]=None
    # return None

# main line
x=['a','b','c','d']
m=3
ids=[None]*m
depth=0                 
global cnt
cnt=0
global mydict
mydict={}

perm2_rec(x,m,ids,depth) 
print(cnt,len(mydict))
for x in mydict:
    print(x,"=",mydict[x])


# arr=[1]
# print(is_unique(arr))

