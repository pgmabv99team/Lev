#Use function to find index of maximum in an array

def mymax(y):
    yl = len(y)
    i = 0
    max = 0
    imax = 0
    #go over all elements of array and find imax (pos. of the maximum)
    while i < yl:
        test = y[i]
        if max < test:
            # new max found
            max = test
            imax = i
        i = i+1
    return imax


x1 = [34, 45, 56, 99999, 101, 34]
x2 = [23, 78, 55, 444, 34, 2332, -92]
x3 = [1, 2, 3, 4]
found = mymax(x1)
print("imax for array x1", found, x1[found])

found = mymax(x2)
print("imax for array x2", found, x2[found])

found = mymax(x3)
print("imax for array x3", found, x3[found])
