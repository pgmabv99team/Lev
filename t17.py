# reading files upcase string/append array 
x=[]
nlines=0
myfile = open("file1.txt", "r")
for myline in myfile:
    mylen=len(myline)-1
    myline2 = myline[0:mylen]+" asdf"
    print(myline2,mylen)
    x.append(myline2.upper())
    # myline2.upper()
    nlines+=1
print("number of lines", nlines,x)