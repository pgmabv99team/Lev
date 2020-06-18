#reverse array order
x = [34, 45, 56, 67, 99, -101]
y = [0, 0, 0, 0, 0, 0]
i = 0
xl = len(x)

while i < xl:
    #y[i]=x[xl-1-i]
    y[xl-1-i]     =x[i]
    print("element", i, x[i],y[i])
    i = i+1
