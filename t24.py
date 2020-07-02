# 2D array
def SumMatrix(p):
    mysum = 0
    nrows=len(p)
    ncols=len(p[0])
    print("number of rows",nrows,"number of columns",ncols)
    irow=0
    while irow<nrows:
        icol=0
        while icol<ncols:
            
            print("cell",irow,icol)
            cell=p[irow][icol]
            print("cell value",cell)
            mysum=mysum+cell
            icol=icol+1
        irow=irow+1
   
   
   
    
    return mysum








yy = [[2, 3, 4],
          [6, 7, 8],
          [456, 54, 65]]
xx = [[2, 5, 4],
          [6, 15, 8]]


xxsum=SumMatrix(xx)
print("sum of Matrix",xxsum)
yysum=SumMatrix(yy)
print("sum of Matrix",yysum)