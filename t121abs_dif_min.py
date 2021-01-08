def solution1(p):
    pl=len(p)
    abs_dif_list=[]
    for i in range(1,pl):

        left=p[0:i]
        right=p[i:]
        left_sum=sum(left)
        right_sum=sum(right)
        abs_dif=abs(left_sum-right_sum)
        abs_dif_list.append(abs_dif)

        # print(left,right,abs_dif)
    mymin=min(abs_dif_list)
    return mymin
# print(solution1([3,1,2,4,3,-5]))




def solution(p):
    pl=len(p)
    abs_dif_list=[]
    left_sum=0
    right_sum=sum(p)
    for i in range(pl-1):

        left_sum +=p[i]
        right_sum -=p[i]
        abs_dif=abs(left_sum-right_sum)
        abs_dif_list.append(abs_dif)

        # print(i,p,left_sum,right_sum,abs_dif)
    mymin=min(abs_dif_list)
    return mymin
print(solution([3,1,2,4,3,-5]))
