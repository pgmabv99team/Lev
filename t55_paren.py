# x=(((1))
# print(x)
y="())(()"
# y="()())(()"
x="(())()"

# for i in range(len(y)):
#     print(y[i])

def paren(p):
    pl=len(p)
    i=0
    left=0
    right=0
    while i<pl:
        if p[i]==")" and left==right:
            print("at",i)
            return False
        
        if p[i]=="(":
            left +=1
        elif p[i]==")":
            right +=1
        
        i +=1
    print(left,right)
    if p[pl-1]=="(":
        return False
    elif right!=left:
        return False
    else:
        return True
# print(paren(y))

def paren_stack(p):
    pl=len(p)
    i=0
    stk=[]
    while i<pl:
        # print("before",stk,p[i])
        if p[i]=="(":
            stk.append(p[i])
        elif p[i]==")" :
            if len(stk)==0:
                print("unbalanced right paren at position",i)
                print(p)
                return False
            else:
                stk.pop()  
            

        print("after",stk)    
        i +=1
    if len(stk)!=0:
        print("unbalanced left paren at position",i)
        print(p)
        return False
# print(paren_stack(x))

def find_number(p,i):
    pl=len(p)  
    j=i
    while j<pl:
        if p[j]=="+" or p[j]=="-":
            break
        j +=1
    t=p[i:j]
    return j,t



def calc(p):
    pl=len(p)
    res=find_number(p,0)
    i=res[0]
    number=res[1]
    mysum=int(number)
    # print(mysum)
    while i<pl-1:
        operator=p[i]
        print("operator",operator)
        i +=1
        res=find_number(p,i)
        j=res[0]
        number=res[1]
        print("number",number)
        
        
        if operator=="+":
            mysum=mysum+int(number)
        elif operator=="-":
            mysum=mysum-int(number)
        print(operator,number,mysum)
        i=j
    print(mysum)
# calc(z)
z="12+11-2-3"
def calc_stack(p):
    pl=len(p)
    stknum=[]
    stkop=[]
    i=0
    res=find_number(p,0)
    i=res[0]
    number=int(res[1])
    stknum.append(number)
    while i<pl:
        
        operator=p[i]
        i +=1
        stkop.append(operator)
        res=find_number(p,i)
        j=res[0]
        number=int(res[1])
        stknum.append(number)
        
        
        
        i=j
    print("numbers",stknum)
    print("operators",stkop)

    while len(stkop)>0:
        print(stknum,stkop)
        operator=stkop.pop(0)
        num1=stknum.pop(0)
        num2=stknum.pop(0)
        if operator=="+":
            num=num2+num1
        elif operator=="-":
            num=num1-num2
        else:
            print("Error")
        stknum.insert(0,num)
    print(stknum)

calc_stack(z)
