x=[1,3,5,7]
def myinsert(q,p):
    i=0
    pl=len(p)
    while i<pl:
        if p[i]>q:
            p.insert(i,q)
            break
        elif q>=p[pl-1]:
            p.append(q)
            break
        else:
            i +=1
    print(p)

    
def myinsert2(q,p):
    i=0
    pl=len(p)
    while i<pl:
        if p[i]>q:
            break

        i +=1
    ins=i
    # insertion index will be where the number will be inserted
    print("original list",p)
    print("insertion index",ins)

    # extend the list
    p.append(None)
    pl=len(p)
    print("extended list",p)

    # loop to shift elements up, in order to make room for our number
    i2=pl-1
    while i2>ins:
        p[i2]=p[i2-1]
        i2 -=1
    
    # inserts number to list
    p[ins]=q
    print("final list",p)

y=[23,-11,5]
for y1 in y:
    myinsert2(y1,x)

