# make  def function to compute the max and the min
# for 2 dimensional matrix.
#dont forget to strt by finding nrows and nols
#google if needed
import numpy
from pandas import *


def MyFunc(p):
    nrows=len(p)
    ncols=len(p[0])
    mymax=p[0][0]
    irows=0
    mymin=p[0][0]
    while irows<nrows:
        icols=0
        while icols<ncols:
            if p[irows][icols]>mymax:
                mymax=p[irows][icols]
            if p[irows][icols]<mymin:
                mymin=p[irows][icols]
            icols=icols+1
        irows=irows+1
    return mymax, mymin


yy = [[11, 33, 45],
      [6, 7, 8],
      [456, 54, 65]]
xx = [[23, 35, 43],
      [6, 15, 8]]
# print(xx)
# print(DataFrame(xx))
    
res=MyFunc(xx)
print(res)
