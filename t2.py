
import matplotlib.pyplot as plt

x  = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y   = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y1  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

l1=len(x)

i=0
while i<l1:
    y[i]=x[i]**2 -10
    y1[i]=10*x[i]
    print(i, x[i], y[i] )
    i=i+1

plt.title(" my plot ")
plt.plot(x, y1)
plt.plot(x, y)

plt.xlabel("My x ")
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid(True)
plt.legend()

plt.show()