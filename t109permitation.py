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

x=['a','b','c','d']
def perm2(p):
    pl=len(p)
    cnt=0
    for i0 in range(pl):
        for i1 in range(pl):
            for i2 in range(pl):
                if i0!=i1 and i1!=i2 and i2!=i0:
                    cnt +=1
                    print(p[i0],p[i1],p[i2])
    print(cnt)
perm2(x) 