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


# def robot1(i,j,n,m,p):
#     if i<n-1:
#         i +=1
#         p[i][j]=1
#         robot1(i,j,n,m,p)
#         p[i][j]=0
#         i -=1
    
#     if j<m-1:
#         j +=1
#         p[i][j]=1
#         robot1(i,j,n,m,p)
#         p[i][j]=0
#         j -=1
#     if i==(n-1) and j==(m-1):
#         mydraw(p)
#         return 
# n=3
# m=4

# p= np.full((n,m),0)
# p[0][0]=1
# robot1(0,0,n,m,p)
# time.sleep(50)  

def robot2(i,j,n,m,step_list,dead_list,p):
    
    if i<n-1:
        c=[i+1,j]
        if c not in dead_list:
            step_list.append("d")
            i +=1
            robot2(i,j,n,m,step_list,dead_list,p)
            i -=1
            step_list.pop()
    if j<m-1:
        c=[i,j+1]
        if c not in dead_list:
            step_list.append("r")
            j +=1
            robot2(i,j,n,m,step_list,dead_list,p)
            j -=1
            step_list.pop()
    if i==(n-1) and j==(m-1):
        print(step_list)
        i1=0
        j1=0
        p[i1][j1]=9
        for step in step_list:
            if step=="r":
                j1 +=1

            if step=="d":
                i1 +=1
            p[i1][j1]=9
        mydraw(p)
        


  
n=3
m=3
p= np.full((n,m),0)



step_list=[]
# dead_list=[[2,0],[1,1],[0,1]]
# dead_list=[[2,2]]
dead_list=[[1,1],[2,0]]
for dead in dead_list:
    i=dead[0]
    j=dead[1]
    p[i][j]=1
print(p)
mydraw(p)

robot2(0,0,n,m,step_list,dead_list,p)
time.sleep(50)