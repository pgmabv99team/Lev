import math
def div(a,b,k):
    i=a
    num=0
    while i<b:
        if i%k==0:
            num +=1
        i +=1
    return num
# print(div(6,11,20))

def div2(a,b,k):
    
    rem=a%k         
    if rem==0:
        # lowest boundary divisible
        m=math.floor((b-a)/k)
        return m+1
    else:
        bef=a-rem
        m=math.floor((b-bef)/k) 
        return m  
        
        
        
        


print(div2(1,11,20))   

print(div2(0,11,20))   

print(div2(1,11,2))                   
print(div2(100,110,10))                   
print(div2(100,110,20))                   
print(div2(100,120,19))                   
print(div2(100,120,29))                   