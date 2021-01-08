# def factor(p):
#     # factors=[]
#     nfactors=0
#     temp=int((p+1)/2)
#     for i in range(1,temp+1):
#         if p%i==0:
#             nfactors +=1
#             # factors.append(i)
#     # factors.append(p)
#     nfactors +=1
#     print(nfactors)
# factor(24)


  
import math 
def solution(n): 
    pfactors=[]
    mycount=[]
    var1=0
    while n % 2 == 0: 
        pfactors.append(2)
        n = n / 2
        var1 +=1
    mycount.append(var1+1)
    temp=int(math.sqrt(n))
    for i in range(3,temp+1,2): 
        var1=0
        while n % i== 0: 
            pfactors.append(i) 
            n = n / i 
            var1 +=1
        mycount.append(var1+1)
        

            
              

    if n > 2: 
        pfactors.append(int(n))
        mycount.append(2)
    prod=1
    for i in mycount:
        prod *=i
    return prod


print(primeFactors(36))