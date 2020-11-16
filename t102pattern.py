def is_vowel(p):
    if p=="a" or p=="e" or p=="o" or p=="i" or p=="u":
        return True
    else:
        return False


def match(str1,pat):
    i=0
    sl=len(str1)
    x=[]
    while i<sl:
        if is_vowel(str1[i])==True:
            x.append("0")
        else:
            x.append("1")
        i +=1
    
    i=0
    good=0
    xl=len(x)
    patl=len(pat)
    while i<xl-patl+1:
        xs=""
        for u in range(patl):
            xs +=x[i+u]
        if xs==pat:
            good +=1
        i +=1
    return good




print(match('heexrutol','0'))


