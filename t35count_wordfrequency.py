# Dictionary of tokenised words

# find key in the dictionary
import util




    
# convert tekeyt string to array of tokens
f = open("data_35.txt", "r", encoding="utf8")
data=f.read()+" "
# print(data)
words = util.make_word_list(data)
print(words)

# build a dictionary key=word, value=count
xDict = {}
for word in words:
    low_word=word.lower()
    found = util.find_key(xDict,low_word)
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
    key_for_max=util.find_mymax_value(xDict)
    print("found at ===",key_for_max,"value ",xDict[key_for_max])
    xDict.pop(key_for_max)
    if i>50:
        break
    