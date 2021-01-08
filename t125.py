def find_pair(p,n):
    dict={}
    for i in p:
        dif=n-i
        if i not in dict:
            dict[dif]=i
        else:
            return i,dif
        

d=[1,2,3,4,5]
print(find_pair(d,7))