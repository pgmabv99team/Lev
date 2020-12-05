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
# x=[2,2,1,2,2]
# print(x,pairs(x))

# x=[2,1,2]
# print(x,pairs(x))

# x=[3,3,4,4,1]
# print(x,pairs(x))

# x=[2,2,9,2,2]
# print(x,pairs(x))

# x=[2,2,2,2,0]
# print(x,pairs(x))

# x=[11,2,2,2,2]
# print(x,pairs(x))

def pairs2(p):
    d={}
    for el in p:
        if el in d:
            d[el] +=1
        else:
            d[el]=1

    for key in d:
        if d[key]%2!=0:
            return key
print(pairs2([1,1,3,3,4]))
