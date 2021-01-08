def perimeter(p):
    per=[]
    for i in range(1,p+1):
        for j in range(1,p+1):
            if j*i==p:
                per.append((j+i)*2)
    return min(per)
# print(perimeter(17))
import math
def solution(n):
    sqrtn=math.sqrt(n)

    
    a=math.floor(sqrtn)
    while a>0:
        if n%a==0:
            b=n/a
            return int((a+b)*2)
        a -=1

print(solution(25))        
    