# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(p):
    pl=len(p)
    i=0
    p.sort()
    if p[i]!=1:
        return 0
    while i<pl-1:
        if p[i]+1==p[i+1]:
            i +=1
            continue
        else:
            return 0
    return 1
x=[1]
print(solution(x))    
