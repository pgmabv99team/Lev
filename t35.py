# Dictionary of tokenised words

# find key in the dictionary
import string
def find_key(xDict, key):
    for word in xDict:
        if word == key:
            return True
    return False

punc=string.punctuation
def make_word_list(p):
    pl = len(p)
    iSep = None
    iBWord = 0
    WordList = []
    for i in range(pl):
        # print(i, p[i])
        # if (p[i] == " ") or (p[i]=="\n") or (p[i]=="!") :
        if (p[i] in punc) or (p[i]=="\n") or (p[i]==" "):
            iSep = i
            myslice=p[iBWord:iSep]
            myslice2=myslice.lower()
            if myslice2 !="the" and  myslice2 != "a" and len(myslice2)>0:
                
                WordList.append(myslice2)
            # print("separator space at position", iSep, p[iBWord:iSep])
            iBWord = iSep+1

    return WordList

def find_mymax_value(p):
    mymax=0
    for key in p:
        if p[key]>mymax:
            mymax=p[key]
            mykey=key

    return mykey
    
# convert tekeyt string to array of tokens
f = open("data_35a.txt", "r")
data=f.read()+" "
# print(data)
words = make_word_list(data)
print(words)

# build a dictionary key=word, value=count
xDict = {}
for word in words:
    low_word=word.lower()
    found = find_key(xDict,low_word)
    if found == True:
        xDict[low_word] = xDict[low_word]+1
    else:

        xDict[low_word] = 1
    # xDict[word] +=1
    # print(found)

# print result
# print(xDict)
dl=(len(xDict))
for i in range(dl):
    key_for_max=find_mymax_value(xDict)
    print("found at ===",key_for_max,"value ",xDict[key_for_max])
    xDict.pop(key_for_max)
