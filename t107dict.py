str1="tasty fat birb birb fat baddad dadbad plant bonk honk bonk clonk donk donk"
words=str1.split()
i=0
d={}
for word in words:
    print(word)
    if word in d:
        d[word]=d[word]+len(word)
    else:2
        d[word]=len(word)
    print(d)
print(d)



