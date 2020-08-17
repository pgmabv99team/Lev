x=[1,2,2,5,7,9,0,0,0,0]
xlen=len(x)
k=2

#find 1st
k1=0
nk=0
for i in range(xlen):
    if(x[i]<k):
        continue
    elif(x[i]==k):
        k1=i
        break
    else:
        break

#find all
print("k1",k1)
if k1==0:
    nk=0
    print("nk",nk)
    exit() 

#1st found
i=k1+1
nk=1
#find rest
while(i<xlen):
    if(x[i]==k):
        nk=nk+1
        i=i+1
        continue
    else:
        break
print("nk final",nk)

nk=0
for i in range(xlen):
    if(x[i]==k):
        nk +=1
    if x[i]>k:
        break

print("nk final",nk)


#find last