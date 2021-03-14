nfiles=2
f=[]
words=[]
lengths=[]
for ifile in range(nfiles):
    file_name="files/folder3/f"+str(ifile+1)+".txt"
    f.append(open(file_name,"r"))
    txt=f[ifile].read()
    split=txt.split()
    sorted_split=sorted(split)
    words.append(sorted_split)
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
    mymin="z"
    for ifile in range(nfiles):
        if pos[ifile]<lengths[ifile]:
            if words[ifile][pos[ifile]]<mymin:
                mymin=words[ifile][pos[ifile]]
                my_ifile=ifile  
    words_all.append(mymin)
    pos[my_ifile] +=1
print(words_all)
    
    

txt_all=" ".join(words_all)
f_all=open("files/folder3/f_all.txt","w")
f_all.write(txt_all)
f_all.close()