# Subtracting elements from one array and adding them to another one (sorting elements of numerous arrays)

def mymax(y):
    yl = len(y)
    i = 0
    max = 0
    imax = 0
    # go over all elements of array and find imax (pos. of the maximum)
    while i < yl:
        test = y[i]
        if max < test:
            # new max found
            max = test
            imax = i
        i = i+1
    return imax


x1 = [34, 45, 56, 99999, -9, 101, 34, 555, -12,1,2,3,4,5,6,7,32,52,42,533453,4534,5,353,6,36,34,63,]
y1 = []
print("starting-------------------->")
i = len(x1)
while i > 0:
    J = mymax(x1)
    print("before", x1)
    print("Terminated", J, x1[J])
    y1.append(x1[J])
    x1.pop(J)
    print("after", x1)

    print("Newborn array", y1)
    i = i-1
