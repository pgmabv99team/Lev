
def stk_paren(p):
    pl=len(p)
    i=0
    stk=[]
    if p[pl-1]=="(":
        print("unpaired left paren at the end of the string")
        return False
    while i<pl:
        if p[i]=="(":
            stk.append(p[i])
        if len(stk)==0 and p[i]==")":
            print("Right paren with no partner. Position:",i,"=",p[i:])
            return False
        elif len(stk)>0 and p[i]==")":
            stk.pop()            
        i +=1
    if stk==[]:
        return True
    else:
        print("False because not empty stack; too many left parens",stk)
        return False


p="((()))"
print(stk_paren(p))
p="("
print(stk_paren(p))
p="(()"
print(stk_paren(p))
p="()())"
print(stk_paren(p))

