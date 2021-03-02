# reading a file in order to find the amount of different words and print them with counts  

# open a file and get the number of lines from the first line
f = open("files/words.txt", "r")
nlines=f.readline()
print(nlines)

d={}
for i in range(int(nlines)):
    read_word=f.readline()

    # removing \n if need be
    l=len(read_word)
    if read_word[l-1]=="\n":
        key=read_word[0:l-1]
    else:
        key=read_word
    
    # check and add to dict
    if key  in d:
        d[key] +=1
    else:
        d[key]=1

# end result
print(len(d))
for key in d:
    print(d[key], end=" ")
print("\ndone")