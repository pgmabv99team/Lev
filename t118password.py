def solution(p):
    ps=p.split(" ")
    # print(ps)
    pl=len(ps)
    i=0
    good_password=[]
    while i<pl:
        word=ps[i]
        if word.isalnum()==False:
            i +=1
            continue

        dig=0
        let=0
        i2=0
        # print(len(word))
        while i2<len(word):
            if word[i2].isalpha()==True:
                let +=1
            elif word[i2].isdigit()==True:
                dig +=1
            i2 +=1
        if dig%2==1 and let%2==0:
            good_password.append(len(ps[i]))
        i +=1
    # print(good_password)
    if len(good_password)==0:
        return -1
    else:
        mymax=max(good_password)
        return mymax
    




print(solution("a"))