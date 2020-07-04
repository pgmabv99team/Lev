# 2D arrays with strings
def MyFunction2(pp):
    numrows = len(pp)
    irows = 0
    
    
    while irows < numrows:
        icols = 0
        numcols = len(pp[irows])
        mymax = len(pp[irows][0])
        while icols < numcols:
            element=pp[irows][icols]
            bob=len(element)
            if bob>mymax:
                mymax=bob
            print(element,len(element),mymax)
            icols = icols+1
        irows = irows+1
        print(mymax)


xx = [["aaaaaa", "cccccc"],
      ["ddddddd", "xxxxxeeeeeeee"]]
MyFunction2(xx)
