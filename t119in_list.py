def in_list(p):
    pl=len(p)
    i=0
    mymin=1
    while i<pl:
        if mymin in p:
            mymin +=1
        i +=1
    return mymin
    

def solution(p):
    p.sort()
    print(p)
    # 1 is before the beginning of the list.
    if p[0]>1:
        return 1
    found=False
    for i in range(len(p)-1):
        l=p[i]
        h=p[i+1]
        if  h>l+1:
            #there is a gap.
            
            if l+1>0:
                found=True
                return l+1
            elif h>1:
                return 1
    # if there is no gap.
    if not found:
        result=p[len(p)-1]+1
        # if list is all negatives
        if result<1:
            return 1
        else:
            return result

[-1000000, 1000000]
# print(in_list2([1,2,3,4,5,6]))
# print(in_list2([1,2,3,4,6]))
# print(in_list2([2,3,4,5,6]))
# print(in_list2([-3,1,2,3,4,5,6]))
# print(in_list2([-5,-4,-3]))    
print(solution([-3,3]))  