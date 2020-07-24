phrase=" even  ate  nine "

def FindBlanks(p):
    pl=len(p)
    iBlank=None
    iBWord=0
    WordList=[]
    for i in range(pl):
        print(i,p[i])
        if p[i]==" ":
            iBlank=i
            if len(p[iBWord:iBlank])>0:
                WordList.append(p[iBWord:iBlank])
            print("blank space at position",iBlank,p[iBWord:iBlank])
            iBWord=iBlank+1

    return WordList
 
    # while i<pl:
    #     print(p[i])
    #     i=i+1

def FindBlanks2(p,start):
    print("Enter FindBlanks2",start)
    pl=len(p)
    iBlank=None
    for i in range(start,pl):
        print(i,p[i])
        if p[i]==" ":
            iBlank=i
            print("blank space at position",i)
            break
    return iBlank
# res=-1
# while True:
#     res=FindBlanks(phrase,res+1)
#     print(res)

#     if res==None:
#         break


res=FindBlanks(phrase)
print(res)