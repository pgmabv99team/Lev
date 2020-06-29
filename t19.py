x=[2,3,4,7,8]
xl=len(x)
i=xl-1
mysum=0
while i>=0:
    mysum=mysum+x[i]
    print("element",i,"is",x[i],mysum) 
    i=i-1
print(mysum)
ave=mysum/xl
print(ave)