def nagaram(a,b):
    a1=sorted(a)
    b1=sorted(b)
    if a1==b1:
        return True
    return False


print(nagaram("dog","god"))
print(nagaram("good","god"))
phrase="dog good dogo birb brib potato god"
class ang_c:
    def __init__(self):
        print("Hello from ang.init")


def nagaram_phrase(phrase):
    wlist=phrase.split()
    word_dict={}
    for i in range(len(wlist)):
        word=wlist[i]
        word1=sorted(word)
        word_key="".join(word1)
        if word_key in word_dict:
            ang=word_dict[word_key]
            ang.word=ang.word+" "+word
            ang.count +=1
            # word_dict[word_key]=ang
            
        else:
            
            ang=ang_c()
            ang.name="Watermelon"
            ang.count=1
            ang.word=word
            word_dict[word_key]=ang

    for key in word_dict:
        obj=word_dict[key]
        print(key,":",obj.name,":",obj.word,":",obj.count)
nagaram_phrase(phrase)

