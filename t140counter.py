# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(n, a):
    d=[0]*n
    mymax=0
    uniform=True
    for i in range(len(a)):
        if a[i]==len(d)+1  :
            # for i2 in range(len(d)):
            #     d[i2]=mymax
            if uniform==False:
                d[0:]=[mymax] * (len(d))
                uniform=True
        
        else:
            d[a[i]-1] +=1
            if d[a[i]-1]>mymax:
                mymax=d[a[i]-1]
                uniform=False
        # print(d)
    return d
print(solution(5,[3,4,4,6,1,4,4,6,6]))

    