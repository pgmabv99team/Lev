
from pandas import *

def mkList(pn):
    px=[]
    i=0
    while i<pn:
        px.append(0)
        i=i+1
    return px


j=0
nrows=5
ncols=5
y=[]
while j<nrows:
    y.append(mkList(ncols))
    j=j+1
print(y)

 
print(DataFrame(y))
print("hi")
irows=0

while irows<nrows:
    icols=0
    while icols<ncols:
        y[irows][icols]=1
        icols=icols+1
    irows=irows+1
print(DataFrame(y))
print("hi")
# print("hi")
# irows=0
# while irows<nrows:
   
#     if irows%2==0:
#         icols=0
#         while icols<ncols:
#             if icols%2==0:
#                 y[irows][icols]=0
#             icols=icols+1
        
#     irows=irows+1
# print(DataFrame(y))

# irows=0
# while irows<nrows:
#     icols=0
#     while icols<ncols:
#         if icols+irows==nrows-1 or icols==irows:             
#                 y[irows][icols]=0
#         icols=icols+1
#     irows=irows+1
# print(DataFrame(y))

i=0
while i<nrows:
    y[i][i]=0
    y[i][nrows-1-i]=0
    i=i+1
print(DataFrame(y))

