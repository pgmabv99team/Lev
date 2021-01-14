def solution(p):
    mydict={}
    abs_num=0
    for i in p:
        if abs(i) not in mydict:
            abs_num +=1
            mydict.update({abs(i):"full"})
    x=mydict.clear()
    print(x)
    return abs_num





d=[-5,-3,-1,0,3,6]
print(solution(d))