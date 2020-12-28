def mydict(p):
    d={}
    count=0
    for x in p:
        if x not in d:
            count +=1
            d[x]="walrus"
    return count

print(mydict(["a","b","b"]))

    