# importing functions

from myfunction import *

x = [-4, -1, -2, -5, -3]
y = [233, -4, -45, -7865, 234]
print(x)
res=MyFunction(x)
resave=res[0]
resmax=res[1]
print("for negatives:average=", resave, "maximum=",resmax)
print(y)
res=MyFunction(y)
resave=res[0]
resmax=res[1]
print("for negatives:average=", resave, "maximum=", resmax)