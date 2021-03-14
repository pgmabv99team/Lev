f=open("files/folder3/f4.txt","r")
count = 0
num_words=[]

while True:
    
 
    line = f.readline()
    if line=="":
        break
    count += 1
    words=line.split()
    d={}
    l=0
    for word in words:
        temp=sorted(word)
        word_s="".join(temp)
        
        if word_s not in d:
            l +=1
            d[word_s]=1
        else:
            d[word_s] +=1
    print(d)
    num_words.append(l)
    
    
    print("Line{}: {}".format(count, line.strip()))
print(num_words)

 
f.close()

