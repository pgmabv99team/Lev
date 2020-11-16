def is_match2(str1,pat):
    # mandatory length of str1 up to "%" needed
    if len(str1)<len(pat)-1:
        return False

    # make str with 9s instead of digits
    sl=len(str1)
    i=0
    str1=[]
    while i<sl:
        if str1[i].isdigit()==False:
            str1.append(str1[i])
        else:
            str1.append("9")
        i +=1
    
    nmatch=0    
    i=0
    patl=len(pat)
    if pat[patl-1]=="%":
        patlm=patl-1
    else:
        patlm=patl
    while i<patlm:
        if str1[i]==pat[i] or pat[i]=="_":
            nmatch +=1
        i +=1
    if nmatch==patlm:
        return True
    else:
        return False



# print(is_match2('at4wetrw','at9%'))
# print(is_match2('hee12rutolvbvbvb','hee99__tol%'))






def is_match3(str1,pat):
    i=0
    patl=len(pat)
    nmatch=0
    ipat=0
    strl=len(str1)
    # assume only 1 dot in pattern
    ndot=1
    while ipat<patl:
        if i>=strl:
            break
        if str1[i]==pat[ipat]:
            # exact match
            nmatch +=1
            i +=1
            ipat +=1
            
        elif pat[ipat]==".":
            if ipat==patl-1:
                # dot is last in pattern/skip rest of str1
                break
            # skipping if "."
            idot=ipat
            i2=i
            # next after dot
            z=pat[idot+1]
            zfound=False
            while i2<strl:
                # choose last match
                if str1[i2]==z:
                    zfound=True
                    i=i2
                i2 +=1
            if zfound==False:
                return False
            nmatch +=1
            ipat +=2
            i +=1
            continue
        else:    
            # didn't match
            ipat +=1
            i +=1

    if nmatch==patl-ndot:
        # all pattern matched except for dots
        return True
    else:
        return False 
    
s="attb"
p="a."
print(s,p)
print(is_match3(s,p))

s="ewdfasdf"
p="asdsada"
print(s,p)
print(is_match3(s,p))

s="wertty"
p="w.ty"
print(s,p)
print(is_match3(s,p))
