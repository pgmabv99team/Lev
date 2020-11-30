
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
                x.append(good)
                
                break
            i2 +=1
        # append length of "0" pattern to x

         
        i +=1
    if len(x)==0:
        mymax=0
    else:
        mymax=max(x)
    print(x)
    return mymax
i=345
print(bin(i),solution(i))

i=31
print(bin(i),solution(i))

        
