# Dictionary of tokenised words

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
        print(i, p[i])
        # if (p[i] == " ") or (p[i]=="\n") or (p[i]=="!") :
        if (p[i] in punc) or (p[i]=="\n"):
            iSep = i
            if len(p[iBWord:iSep]) > 0:
                WordList.append(p[iBWord:iSep])
            print("separator space at position", iSep, p[iBWord:iSep])
            iBWord = iSep+1

    return WordList

# convert text string to array of tokens
f = open("data_35.txt", "r")
data=f.read()+" "
print(data)
phrase = " even  ate  nine potato Lev BIGGER BADDER BETTER Lev Lev Epic LevLev "
words = make_word_list(data)
print(words)

# build a dictionary key=word, value=count
xDict = {}
for word in words:
    found = find_key(xDict, word)
    if found == True:
        xDict[word] = xDict[word]+1
    else:
        xDict[word] = 1
    # xDict[word] +=1
    print(found)

# print result
print(xDict)


print(punc)