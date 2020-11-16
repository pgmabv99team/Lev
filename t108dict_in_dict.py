import json
p="pow wow cow cow birb BiRb pOTtATo potato "
d={}
words=p.split()
for word in words:
    word2=word.lower()
    if word2 not in d:
        urlg="https://www.google.com/search?q="+word2
        urlw="https://en.wikipedia.org/wiki/"+word2
        urlb="https://www.bing.com/search?q="+word2
        tmpd={}
        tmpd["urlg"]=urlg
        tmpd["urlw"]=urlw
        tmpd["urlb"]=urlb
        tmpd["count"]=1
        d[word2]=tmpd
    else:
        d[word2]["count"] +=1
     
print(d)
for key in d:
    print(key,json.dumps(d[key],indent=4))
s="https://www.google.com/search?q=potato"
