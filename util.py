
import string
# make word list
punc=string.punctuation
def make_word_list(p):


    pl = len(p)
    ForDeleting=["the","and","or","for","a","of","in","to","is","from"]
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
            # if myslice2 !="the" and  myslice2 != "a" and myslice2 !="or" and len(myslice2)>0:
            if myslice2 not in ForDeleting and len(myslice2)>0:
                WordList.append(myslice2)
            # print("separator space at position", iSep, p[iBWord:iSep])
            iBWord = iSep+1

    return WordList

# find key in the dictionary
def find_key(xDict, key):
    for word in xDict:
        if word == key:
            return True
    return False

# find max value in Dict
def find_mymax_value(p):
    mymax=0
    for key in p:
        if p[key]>mymax:
            mymax=p[key]
            mykey=key

    return mykey

# Bubble Lists
def list_sort(p):
    a=0
    
    while True:
        nswap=0
        for i in range(len(p)-1):
            
            if p[i+1]<p[i]:
                a=p[i+1]
                p[i+1]=p[i]
                p[i]=a
                nswap=nswap+1
        if nswap==1 or nswap==0:
            break

# merge 2 sorted lists into 1
def merge_lists(xp,yp):
    zp=[]
    print("xp=",xp)
    print("yp=",yp)
    ixp=0
    iyp=0
    xpl=len(xp)
    ypl=len(yp)
    while True:
        # print(ixp,iyp)
        
        if ixp>=xpl and iyp>=ypl:
            # both lists are finished
            break
        if ixp>=xpl:
            # xplist is over but yplist is not, so take from yp
            zp.append(yp[iyp])
            iyp=iyp+1
            continue
        if iyp>=ypl:
            # yplist is over but xplist is not, so take from xp
            zp.append(xp[ixp])
            ixp=ixp+1
            continue
        if xp[ixp]>yp[iyp]:
            zp.append(yp[iyp])
            iyp=iyp+1
        else:
            zp.append(xp[ixp])
            ixp=ixp+1
        # print(zp)
    return zp


# print top words in a file
def print_top_words(filename):
    # convert tekeyt string to array of tokens
    f = open(filename, "r", encoding="utf8")
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
        if i>50:
            break


# efficient swap
def swap(x,m,n):
    a=x[m]
    x[m]=x[n]
    x[n]=a

# swap 2D
def swap_in_row(x,row,m,n):
    a=x[row][m]
    x[row][m]=x[row][n]
    x[row][n]=a

# swap up/down
def swap_in_column(x,column,m,n):
    a=x[m][column]
    x[m][column]=x[n][column]
    x[n][column]=a
