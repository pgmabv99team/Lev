def age(p,q):
    max_year=0
    max_year_count=0
    for year in range(1900,2000):
        count=0
        for ip in range(len(p)):
            
            if p[ip]<=year and q[ip]>=year:
                count +=1
        if count>max_year_count:
            max_year_count=count
            max_year=year
    return max_year
# birth=[1985,1906,1955]
# death=[1995,1987,1999]
# print(age(birth,death))

def age2(p,q):
    mydict={}
    for ip in range(len(p)):
        for year in range(p[ip],q[ip]+1):
            if year not in mydict:
                mydict[year]=1
            else:
                # mydict[year]=mydict[year]+1

                mydict[year]=mydict.get(year)+1
    
    # print(mydict)
    return max(mydict, key=mydict.get)
# print(age2(birth,death))


from random import seed
from random import randint

n=10**6
# seed(1)
seed(None)
birth=[]
death=[]
for ip in range(n):
    birth.append(randint(1900,2000))
    death.append(randint(birth[ip],2000))
import time

t1=time.time()
print(age(birth,death))
t2=time.time()
print(t2-t1)

t1=time.time()
print(age2(birth,death))
t2=time.time()
print(t2-t1)