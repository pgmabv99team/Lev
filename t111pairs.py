def pairs(p):
    i=0
    tmp=p.copy()
    while True:
        if len(tmp)==1:
            break
        mybreak=None
        i2=i+1
        while i2<len(tmp):
            if tmp[i2]==tmp[i]:
                tmp.pop(i)
                i2=i2-1
                tmp.pop(i2)
                mybreak=True
                break
            else:
                mybreak=False
            i2 +=1
        if mybreak==False:
            i +=1
    return tmp[0]
x=[2,2,1,2,2]
print(x,pairs(x))

x=[2,1,2]
print(x,pairs(x))

x=[3,3,4,4,1]
print(x,pairs(x))

x=[2,2,1,2,2]
print(x,pairs(x))

x=[2,2,2,2,1]
print(x,pairs(x))

y=3