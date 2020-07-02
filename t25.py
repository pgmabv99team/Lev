def MatrixMax(pp):


    numrows = len(pp)

    irows = 0
    mysum = 0
    mymax = None

    while irows < numrows:
        icols = 0
        numcols = len(pp[irows])
        print(numcols)
        while icols < numcols:
            if pp[irows][icols] % 2 == 1:

                mysum = mysum+pp[irows][icols]
                if mymax == None:
                    mymax = pp[irows][icols]
                else:
                    if pp[irows][icols] > mymax:
                        mymax = pp[irows][icols]

            icols = icols+1
        irows = irows+1
    return mysum,mymax


xx = [[2, 3, 4],
    [3, 3333, 5,54]]

res=MatrixMax(xx)
print(res)
print("mysum",res[0],"mymax",res[1])