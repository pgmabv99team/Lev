
def solution(p):
    bp=bin(p)
    sp=str(bp)
    sp=sp[2:]
    pl=len(sp)
    i=0
    x=[]
    while i<pl:
        good=0
        i2=i
        # look forward and count consecutive zeroes
        while i2<pl:
            if sp[i2]=="0":
                good +=1
            else:
                break
            i2 +=1
        # append length of "0" pattern to x

        x.append(good)
        i +=1
    return max(x)
print(bin(32))
print(solution(32))
        
