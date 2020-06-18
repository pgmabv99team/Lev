x = ["hellooooooooooooooooooooooooooooo","Good,a,bye","walrus","banNana,boomerang","a"]
xl=len(x)
i=0
max=0
imax=0
while i<xl:
    el=x[i]
    test=len(el)
    print("element",i,el,test)
    if max>=test:
        print("no new max")
    else:
        max=test
        imax=i
        print("new max",max)
    i=i+1
print("final max",max,"position",imax,x[imax])
# print(x[imax-1],x[imax+1])
print(xl,i)
if imax==0:
    n1="none"
else:
    n1=x[imax-1]
    
if imax==xl-1:
    n2="none"
else:
    n2=x[imax+1]
print(n1,n2)
