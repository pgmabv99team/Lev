import util


x=[-12,23,42,563]
y=[23,12,1231231,2322323,4545]
util.list_sort(x)
util.list_sort(y)
z=[]
print("x=",x)
print("y=",y)
while True:
    if x[0]>y[0]:
        z.append(y[0])
        y.pop(0)
        if len(y)==0: 
            # trigger end processing with remainder of x
            z.extend(x)
            x=[]
            break
    else:
        z.append(x[0])
        
        x.pop(0)
        if len(x)==0:
            # trigger end processing with remainder of y
            z.extend(y)
            y=[]
            break
print("after loop")
print("x=",x,"y=",y)
print(z)