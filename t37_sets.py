# set operations
xlist=["a","c","d"]
ylist=["a","b","c","f"]
zlist-[]
ly=len(ylist)
for y in ylist:
    for x in xlist:
        if y==x:
            zlist.append(x)
print(zlist)

zlist=[]
for x in xlist:
    if x in ylist:
        zlist.append(x)
print("intersection x*y",zlist)

zlist=[]
for x in xlist:
    if x not in ylist:
        zlist.append(x)
print("x-y ",zlist)

zlist=[]
for y in ylist:
    if y not in xlist:
        zlist.append(y)
print("y-x",zlist)

zlist=[]
for y in ylist:
    zlist.append(y)
for x in xlist:
    if x not in zlist:
        zlist.append(x)
print("y+x excluding copies ", zlist)

zlist=[]
for y in ylist:
    if y not in xlist:
        zlist.append(y)
for x in xlist:
    if x not in ylist:
        zlist.append(x)
print("symmetric difference of x and y", zlist)