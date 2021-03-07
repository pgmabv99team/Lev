f1=open("files/folder3/f1.txt","r")
txt1=f1.read()
words1=txt1.split()

f2=open("files/folder3/f2.txt","r")
txt2=f2.read()
words2=txt2.split()
l1=len(words1)
l2=len(words2)
if l1>l2:
    short=l2
else:
    short=l1

words_all=[]
for i in range(short):
    words_all.append(words1[i])
    words_all.append(words2[i])
# print(i)
if short==l2:
    words_all +=words1[i:]
else:
    words_all +=words2[i:]
print(words_all)

txt_all=" ".join(words_all)
f_all=open("files/folder3/f_all.txt","w")
f_all.write(txt_all)
f_all.close()