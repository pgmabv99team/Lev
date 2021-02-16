def cars(p):
    count=0
    for i in range(len(p)):
        if p[i]==0:
            for i2 in range(i,len(p)):
                if p[i2]==1:
                    count +=1
    if count>1000000000:
        return -1
    return count

print(cars([1,1,0]))