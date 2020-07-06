#  1.copy all elemennts from xx1 to yy using append, print result
#  2.the same copy , but in reverse order : 3,2 1
#  3. pop values from xx1 that have even index , i,e xx1[0], xx1[2], etc
#  4. pop values from xx1 that have even  value , i,e xx1[1]=2, xx1[4]=8, etc
xx1=["a","b","c","d","e"]
yy=[]
xl=len(xx1)

# while i<xl:
#     print("element",xx1,xx1[i])
#     yy.append(xx1[i])
#     i=i+1

# print(yy)
# i=xl-1

# while i>=0:
    
#     yy.append(xx1[i])
#     i=i-1
# print(yy)

# i=0
# while i<xl:
    

#     if xx1[i]%2==1:
#         xx1.pop(i)
#         xl=len(xx1)
        
    
#     i=i+1

# print(xx1)


i=0
while i<xl:
    

    if i%2==1:
        
        yy.append(xx1[i])
        
        
 
    i=i+1
    
print(xx1)
print(yy)