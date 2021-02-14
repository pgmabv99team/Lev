import numpy as np
import matplotlib.pyplot as plt
import time
import math
from numpy.core.shape_base import block


def mydraw(test):
    plt.clf()
    plt.imshow(test)
    plt.colorbar()
    plt.show(block=False)
    plt.pause(.001)


def visual(n, m, step_list, dead_list):
    p = np.full((n, m), 0)
    print(step_list)
    i1 = 0
    j1 = 0
    p[i1][j1] = 9
    for step in step_list:
        i = step[0]
        j = step[1]
        p[i][j] = 9

    for dead in dead_list:
        i = dead[0]
        j = dead[1]
        p[i][j] = 5

    mydraw(p)
    print(p)


def robot2(i, j, n, m, step_list_1, dead_list, step_list_2):

    if i < n-1:
        c = [i+1, j]
        if c not in dead_list:
            step_list_1.append("d")
            step_list_2.append([i+1, j])
            i += 1
            robot2(i, j, n, m, step_list_1, dead_list, step_list_2)
            i -= 1
            step_list_1.pop()
            step_list_2.pop()
    if j < m-1:
        c = [i, j+1]
        if c not in dead_list:
            step_list_1.append("r")
            step_list_2.append([i, j+1])
            j += 1
            robot2(i, j, n, m, step_list_1, dead_list, step_list_2)
            j -= 1
            step_list_1.pop()
            step_list_2.pop()

    if i == (n-1) and j == (m-1):
        visual(n, m, step_list_2, dead_list)


n = 4
m = 4


step_list_1 = []
step_list_2 = []
# dead_list=[[2,0],[1,1],[0,1]]
# dead_list=[[2,2]]
dead_list = []


# robot2(0,0,n,m,step_list_1,dead_list,step_list_2)
# time.sleep(50)

def robot3(n,m,stop):
    p = np.full((n, m), 0)
    # for i in range(n):
    #     p[i][i]=2
    #     mydraw(p)

    # for i in range(n):
    #     p[i][n-1-i]=7
    #     mydraw(p)

    # for i in range(n):
    #     p[i][i]=2
    #     p[i][n-1-i]=7
    #     mydraw(p)

    # for i in range(int(n/2),-1,-1):
    #     p[i][int(n/2)]=2
    #     p[int(n/2)][i]=2
    #     p[i][i]=7
    #     p[n-1-i][n-1-i]=7

    #     # p[(int(n/2))-i-1][(int(n/2))-i-1]=7
    #     # p[(int(n/2))+i][(int(n/2))+i]=7

    #     # p[i][n-1-i]=8
    #     # p[n-1-i][i]=8

    #     mydraw(p)

    # for i in range(n):
    #     p[0][i]=1
    #     p[n-1][n-1-i]=2
    #     p[i][n-1]=3
    #     p[n-1-i][0]=4
    #     mydraw(p)
    # for k in range(n):
    #     for i in range(k,n-k):
    #         p[k][i]=1
    #         p[n-1-k][i]=4
    #         p[i][k]=7
    #     mydraw(p)
    i = 0
    j = 0

    istep = 1
    jstep=1
    break_time=0
    while True:
        # time.sleep(1)

        color = 4
        if istep<0:
            color = 9

        p[i][j] = color
        # mydraw(p)
        # print(p)
        # print(i)
        # check current direction
        if istep > 0:
            # Did we hit the upper limit?
            if i+istep <= n-1:
                # No, keep going.
                i += istep
            else:
                # stay in place, reverse direction
                istep = -istep
                mydraw(p)
        else:
            #  Did we hit lower limt???!?!!?!?!?
            if i+istep >= 0:
                i += istep
                # No!
            else:
                istep = -istep
                mydraw(p)
                # Stay hydrated
                break_time +=1
        # check current direction
        if jstep > 0:
            # Did we hit the upper limit?
            if j+jstep <= m-1:
                # No, keep going.
                j += jstep
            else:
                # stay in place, reverse direction
                jstep = -jstep
                jstep -=1
                mydraw(p)
        else:
            #  Did we hit lower limt???!?!!?!?!?
            if j+jstep >= 0:
                j += jstep
                # No!
            else:
                jstep = -jstep
                jstep +=1
                mydraw(p)
                # Stay hydrated
                break_time +=1
        if break_time==stop:
            break



# robot3(100,200,15)
# time.sleep(50)

def robot4(n,k,p):
    
    ctr=int(n/2)
    for i in range(ctr-k,ctr+k+1):
        p[i][ctr-k]=1
        p[ctr-k][i]=2
        p[i][ctr+k]=3
        p[ctr+k][i]=4

        mydraw(p)
        print(p)
# robot4(50,12)
# time.sleep(50)
# n=50
# p=np.full((n, n), 0)
# for k in range(0,15,2):
#     robot4(n,k,p)

def robot5(n):
    p=np.full((n, n), 0)
    for i in range(n):
        j=int(math.sqrt(n**2-i**2))-1
        print(i,j)
        p[i][j]=1
    mydraw(p)
    
robot5(1000)
time.sleep(50)