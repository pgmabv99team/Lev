x = [1,3,2,7,9,-12,13]

xl=len(x)
i=0
s=0
min=0
max=0
while i<xl:
    s=s+x[i]
    # if min>x[i]:
    #     min=x[i]
    # print("minimum", min)
    if max<x[i]:
        max=x[i]
    print(i, x[i])
    print("maximum",max)
    i=i+1

a=s/i
print("average", a)

print("sum", s)