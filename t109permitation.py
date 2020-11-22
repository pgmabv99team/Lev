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


def is_unique(nums):
    nl=len(nums)
    x={}
    for num in range(nl):
        mykey=nums[num]
        if mykey in x:
            return False
        else:
            x[mykey]=nums[num]
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
# permitation with recursion
def perm2_rec(p,m,ids,depth):
    pl=len(p)
    global cnt
    for i0 in range(pl):
        ids[depth]=i0
        if depth==m-1:
            # full depth reached
            if is_unique(ids):
                # ids are unique
                cnt +=1
                print(ids)
                for id in ids:
                    print(p[id],end=" ")
                print("\n")
        else:
            # depth not reached. call func again
            perm2_rec(p,m,ids,depth+1)

x=['a','b','c','d','e']
m=3
ids=[0]*m
depth=0    
global cnt
cnt=0
perm2_rec(x,m,ids,depth) 
print(cnt)


# arr=[1]
# print(is_unique(arr))

