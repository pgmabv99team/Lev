uncouth=open("files/uncouthlanguage.txt","r")
uncouth_txt=uncouth.read()
uncouth_words=uncouth_txt.split(" ")

f1 = open("files/test.txt", "r")
txt=f1.read()
words=txt.split(" ")
# print(words)

l=len(words)
words2=[]
for i in range(l):
    word=words[i]
    # print(word)
    if words[i] in uncouth_words:
        continue
    words2.append(words[i])
# print(words2)
txt2=" ".join(words2)
# print(txt2)

f2=open("files/test2.txt","w")
f2.write(txt2)
f2.close()

        
