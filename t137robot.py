import numpy as np
import matplotlib.pyplot as plt
import time

from numpy.core.shape_base import block

def mydraw(test):
    plt.clf()
    plt.imshow(test)
    plt.colorbar()
    plt.show(block=False)
    plt.pause(1)
    

# n =11
# test= np.full((n,n),0)
# for i in range(n):
#     test[i,i]=1
#     test[n-i-1,i]=9

#     # mydraw(test)
    

# def robot(i,j,n,m):
#     p= np.full((n,m),0)
#     p[i][j]=1
#     mydraw(p)
#     i1=i
#     j1=j
#     while True:

        
#         if i1<n-1:
#             i1 +=1
#             p[i1][j1]=1
#             mydraw(p)
#         if j1<m-1:
#             j1 +=1
#             p[i1][j1]=1
#             mydraw(p)
#         if i1==(n-1) and j1==(m-1):
#             break
# robot(0,0,3,10)
# time.sleep(50)  


def robot1(i,j,n,m,p):
    if i<n-1:
        i +=1
        p[i][j]=1
        robot1(i,j,n,m,p)
        p[i][j]=0
        i -=1
    
    if j<m-1:
        j +=1
        p[i][j]=1
        robot1(i,j,n,m,p)
        p[i][j]=0
        j -=1
    if i==(n-1) and j==(m-1):
        mydraw(p)
        return 
n=3
m=4

p= np.full((n,m),0)
p[0][0]=1
robot1(0,0,n,m,p)
time.sleep(50)  