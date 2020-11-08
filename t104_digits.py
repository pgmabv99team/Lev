def count_in(n):
    # convert to string
    p=str(n)
    pl=len(p)
    
    
    # make a list from that string
    # x=[]
    # i=0
    # while i<pl:
    #     x.append(p[i])
    #     i +=1
    # print(x)

    # # turn each element of list into int() and add it to sum
    # i=0
    # xl=len(x)
    # mysum=0
    # while i<xl:
    #     temp=int(p[i])
    #     mysum=mysum+temp
    #     i +=1

    # mysum=0
    # i=0
    # while i<pl:
    #     temp=int(p[i])
    #     mysum=mysum+temp
    #     i +=1
        
    mysum=0
    for i in range(pl):
        temp=int(p[i])
        mysum +=temp
    return mysum

print(count_in(234))
