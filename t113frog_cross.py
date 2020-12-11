# frog crossing river
def solution(x,a):
    al=len(a)
    i=0
    b=[0]*x
    # print(b)
    filled=0
    goal=False
    while i<al:
        leaf_pos=a[i]
        if leaf_pos>x:
            i +=1
            continue

        if b[leaf_pos-1]==0:                     
            filled +=1
            b[leaf_pos-1]=1

        # print(b)

        if filled==x:
            goal=True
            break
        
       
        i +=1
    if goal==True:
        return i
    else:
        return -1

print(solution(3,[1,33,44,2,3]))

# A[0] = 1
# A[1] = 3
# A[2] = 1
# A[3] = 4
# A[4] = 2
# A[5] = 3
# A[6] = 5
# A[7] = 4