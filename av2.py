import numpy as np

# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print(a)
# b = a[:,2:2]
# print(b)

a=np.array([[1,2,3],[4,5,6]])

print(a)
b=np.array([2,2,2])
print(b)
print("add",np.add(a,b))
print("a+b",a+b)
print("mult",np.multiply(a,b))
print("a*b",a*b)
# b=a[:,np.newaxis]
# print(b)
# c=a[np.newaxis,:]
# print(c)
# ap=a+2
# print(ap)