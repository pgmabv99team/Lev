xList=[23,34,35]
# print(xList[0]*2)

# for x in xList:
#     print(x,x*2)
# print(len(xList))
xl=len(xList)
# yList=[]


# xList.insert(0,"walrus")
# xList.insert(0,"walrus")
# xList.insert(2,"cabbage")
# a=xList.index("walrus")
# print(xList,a)

# for i in range(len(words)):
#     print(words[i])


def find_key(xDict,key):
    for word in xDict:
        if word==key:
            return True
    return False
    





# xDict={"papa":1}

# res=find_key(xDict,"papa")
# print("result:",res)
# res=find_key(xDict,"mama")
# print("result:",res)

xDict={}
words=["Papa","Mama","Lev","Whiskey","Lev"]
for word in words:
    found=find_key(xDict,word)
    if found==True:
        xDict[word]=xDict[word]+1
    else:
        xDict[word]=1
    # xDict[word] +=1
    print(found)
print(xDict)




# # T=10
# # n=0

# # for n in range(T):
# #     xDict["Lev"]=xDict["Lev"]+1
# #     xDict["Whiskey"]=xDict["Whiskey"]+1

# for key in xDict:
#     xDict[key]=xDict[key]+10


# print(xDict)
# for key in xDict:
#     print(key,xDict[key])