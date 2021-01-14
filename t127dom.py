def dominator(p):
    dict={}
    for i in range(len(p)):
        if p[i] not in dict:
            dict[p[i]]=1

        else:
            dict[p[i]] +=1
        if dict[p[i]]>len(p)/2:
            return i
    return -1

            
d=[3,4,3,2,3,-1,3,3]
# d=[1,2,3]
# d=[1]
print(dominator(d))