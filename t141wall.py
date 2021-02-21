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

def square(n):
    p = np.full((n, n), 0)
    mydraw(p)

# square(4)
# time.sleep(50)

def draw_wall(w):
    jmax=max(w)
    imax=len(w)
    p=np.full((imax,jmax),0)
    for i in range(imax):
        print(i)
        h=w[i]
        for j in range(h):
            p[i][j]=1
        mydraw(p)
    # h=min(w)    
    # for i in  range(imax):
    #     for j in range(h):
    #         p[i][j]=4
    #     mydraw(p)
    

        


w=[8,8,5,7,9,8,7,4,8]
draw_wall(w)
mymin=min(w)
for i in range(len(w)):
    w[i] -=mymin
draw_wall(w)
time.sleep(50)