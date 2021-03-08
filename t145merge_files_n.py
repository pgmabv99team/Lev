nfiles=3
f=[]
words=[]
lengths=[]
for ifile in range(nfiles):
    file_name="files/folder3/f"+str(ifile+1)+".txt"
    f.append(open(file_name,"r"))
    txt=f[ifile].read()
    words.append(txt.split())
    lengths.append(len(words[ifile]))
print("words",words)
print("lengths",lengths)
long=max(lengths)
words_all=[]
pos=[0]*nfiles

 
stop=False 
while True:
    for ifile in range(nfiles):
        if pos[ifile]==long:
            stop=True
    if stop==True:
        break
    for ifile in range(nfiles):
        if pos[ifile]<lengths[ifile]:
            
            temp=words[ifile][pos[ifile]]
            words_all.append(temp)
            pos[ifile] +=1
print(words_all)
    
    

txt_all=" ".join(words_all)
f_all=open("files/folder3/f_all.txt","w")
f_all.write(txt_all)
f_all.close()