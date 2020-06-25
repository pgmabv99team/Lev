# 2D array (sum,min,max)

x = [
    [-11, -12],
    [21, 22],
    [31, 32]
]
# print(x[1][2])
nc = len(x[0])
nr = len(x)
#print(nc, nr)
sum = 0
max = x[0][0]
min = x[0][0]
ir = 0
while ir < nr:
    ic = 0
    while ic < nc:
        sum = sum+x[ir][ic]
        if x[ir][ic] > max:
            max = x[ir][ic]
        if x[ir][ic] < min:
            min = x[ir][ic]
        ic = ic+1

    ir = ir+1
print(sum, max, min)
