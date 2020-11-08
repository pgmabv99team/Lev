words=["aa","bb","cc","aa"]
d={}
for word in words:
    print(word)
    if word in d :
        d[word] +=1
    else:
        d[word] =1

print(d)
for key in d:
    print(key,"is hereby found to be",d[key])
