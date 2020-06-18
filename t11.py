#Array append/pop 
#Array pop till reduced to nothing
#New while loop
x=["potato","MajestikBirb","Beer","WhIsKey BOrB"]
y=[]
i=0
xl=len(x)
y.append("aaaaaaa")
#y.append("or")
while i<xl:
    y.append("or")
    y.append(x[i])
    
    #print("element",i,y[i+1])
    i=i+1
y.append("or")
y.append("zzzzzz")
print(y)
y.pop()
print(y)

# yl=len(y)
# i=0
# while i<yl:
#     y.pop()
#     print(y)
#     i=i+1
# print(y)

while len(y)>0:
    y.pop()
    print(y)
print(y)
