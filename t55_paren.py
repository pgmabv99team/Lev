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

z="1+24+34-56"
def calc(p):
    pl=len(p)
    i=1
    mysum=int(p[0])
    # print(mysum)
    while i<pl-1:
        j=i+1
        while j<pl:
            if p[j]=="+" or p[j]=="-":
                break
            
            j +=1
        t=p[i+1:j]
        print("t",t)
        print("operator",p[i])
        
        if p[i]=="+":
            mysum=mysum+int(t)
        elif p[i]=="-":
            mysum=mysum-int(t)
        print(p[i],t,mysum)
        i=j
    print(mysum)
calc(z)