def minpop(p):
    pl=len(p)
    mymin=p[0]
    imin=0
    for i in range(pl):
        if p[i]<mymin:
            mymin=p[i]
            imin=i

   
    p.pop(imin)
    return mymin,imin

def solution2(p):
    pl=len(p)
    ave_list=[]
    i_list=[]
    for i1 in range(pl):

        for i2 in range(i1+1,pl):
            
            s=p[i1:i2+1]
            sl=len(s)

            print(i1,i2,sl)
            print(i1,i2,s)

            ave_list.append(sum(s)/sl)
            i_list.append(i1)
    res=minpop(ave_list)
    
    return  i_list[res[1]]

d=[4, 2, 2, 5, 1, 5, 8]
# print(solution(d))








def solution3(p):
    pl=len(p)
    mymin_ave=10001
    mymin_pos=None
    for i1 in range(pl):
        mysum=p[i1]
        mycount=1
        for i2 in range(i1+1,pl):
            


            # print(i1,i2)
            
            mysum=mysum+p[i2]
            mycount +=1
            myave=mysum/mycount
            if myave<mymin_ave:
                mymin_ave=myave
                mymin_pos=i1
    
    return  mymin_pos

d=[4, 2, 2]
print(solution3(d))



import numpy
# array = numpy.array([49, 51, 53, 56])


def solution(p):
    pl=len(p)
    mysum_list=[]
    mycount_list=[]
    myave_list=[]
    mysum=p[0]
    for i1 in range(1,pl):
        mysum=mysum+p[i1]
        mysum_list.append(mysum)
        mycount_list.append(i1+1)
        myave_list.append(mysum/(i1+1))
    
    print(mysum_list,mycount_list,myave_list)
    for i2 in range(1,pl):
        for i3 in range(pl-1):
            mysum_list[i3] -=p[i2]
        print(mysum_list)


d=[4, 2, 2,3]
print(solution(d))