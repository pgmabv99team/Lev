import numpy as np
import matplotlib.pyplot as plt

def cov(x,y):
    xm =x.mean()
    ym =y.mean()
    cx=x-xm
    cy=y-ym
    c=cx*cy
    s=np.sum(c)
    res=s/(len(x)-1)
    return res

def covmat(x,y):
    covm =np.array([         \
        [cov(x,x),cov(x,y)], \
        [cov(y,x),cov(y,y)]  \
                  ])
    return covm

# x=np.array([2,2,3])
# y=np.array([10,10,11])
x=np.random.normal(0, 1, 500)
y=np.random.normal(0, 1, 500)
cov1=cov(x,y)
print(cov1)
covmat1=covmat(x,y)
print(covmat1)
print(x)