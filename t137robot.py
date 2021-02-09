import numpy as np
import matplotlib.pyplot as plt
import time

from numpy.core.shape_base import block


def mydraw(test):
    plt.clf()
    plt.imshow(test)
    plt.colorbar()
    plt.show(block=False)
    plt.pause(.0000001)


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

def robot3(n):
    p = np.full((n, n), 0)
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
    jstep = 0
    print(p)
    while True:
        
        if istep > 0:
            p[i][j] = 1
            mydraw(p)
            print(p)
            if i+istep <= n-1:
                i += istep
                
                
            else:
                istep=-istep
        if istep<0:
            p[i][j]=2
            mydraw(p)
            print(p)
            if i+istep>=0:
                i +=istep
                
            else:
                istep=-istep
    #    mydraw(p)


robot3(10)
time.sleep(50)
