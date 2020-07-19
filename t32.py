# make  def function to compute the max and the min
# for 2 dimensional matrix.
# using "for" loop
import numpy
from pandas import *


def MyFunc(p):
    nrows=len(p)
    ncols=len(p[0])
    mymax=p[0][0]
    mymin=p[0][0]
    for irows in range(nrows):
        for icols in range(ncols):
            if p[irows][icols]>mymax:
                mymax=p[irows][icols]
            if p[irows][icols]<mymin:
                mymin=p[irows][icols]


            

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
