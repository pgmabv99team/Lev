# 2D array (Column totals, row totals, complete totals)

x = [
    [-11, -12],
    [21, 22],
    [31, 32]
]
# print(x[1][2])
nc = len(x[0])
nr = len(x)
#print(nc, nr)
TotSum = 0
TotMax = x[0][0]
TotMin = x[0][0]
ic = 0
while ic < nc:
    print("Starting inside loop")
    ColSum = 0
    ColMax = x[0][ic]
    ColMin = x[0][ic]
    ir = 0
    while ir < nr:
        ColSum = ColSum+x[ir][ic]
        if x[ir][ic] > ColMax:
            ColMax = x[ir][ic]
        if x[ir][ic] < ColMin:
            ColMin = x[ir][ic]
        ir = ir+1
    print("ColSum", ColSum, "ColMin", ColMin, "max", max)
    TotSum = TotSum+ColSum
    if ColMax > TotMax:
        TotMax = ColMax
    if ColMin < TotMin:
        TotMin = ColMin
    ic = ic+1
print("Total Sum", TotSum, "Final Max", TotMax, "Final Min", TotMin)
