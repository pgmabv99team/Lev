
import numpy as np 
from numpy import newaxis

npa= np.array([36.5, 37, 37.5, 38, 39])
a = [36.5, 37, 37.5, 38, 39]

def t2(x):
    res=2*x
    return(res) 

print("npa*2",t2(npa))
print("a*2",t2(a))


import re
x = re.search(".rix","A rat and a rat can't be friends.")
print(x)