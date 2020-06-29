# nested "ifs", swap practice,
# find the sum,ave, and min of positive numbers in an array
x = [-4, -1, -2, -5, -3]
xl = len(x)
# j=0
# while j<xl:
#     i=0
#     mswaps=0
#     while i<xl-1:
#         print("element",i,x[i],x[i+1])
#         if x[i]>x[i+1]:
#             print("before swap",x[i],x[i+1])
#             a=x[i]
#             x[i]=x[i+1]
#             x[i+1]=a
#             print("after swap",x[i],x[i+1])
#             mswaps +=1


#         i=i+1
#     print(x,mswaps)
#     if mswaps==0:
#         break
#     j=j+1


print("final array", x)
i = 0
sum = 0
nneg = 0
# find the first positive
j = 0
while j < xl:
    if x[j] < 0:
        break
    j = j+1
if j<xl:
    mymax=x[j]
else:
    mymax="no luck......try again?"

# main loop
while i < xl:
    if x[i] < 0:
        # working on sum
        sum = sum+x[i]
        nneg += 1
        # working on min
        if x[i] > mymax:
            mymax = x[i]
    i = i+1


if nneg>0:
    ave=sum/nneg
else:
    ave="|-|OLY SHIT THIS TOOK A LONG TIME"
print(ave,mymax)
