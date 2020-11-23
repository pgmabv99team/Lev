x=9<<10
print(format(x, '016b'))

class per:

    def __init__(self):
        self.name="av"

p=per()
plist=[]
plist.append(p)
plist.append(p)
print(plist[1].name)
plist[0].name="xxx"
print(plist[1].name)
plist[1].name="zzzz"
print(plist[0].name)

z=[12,3]
y=str(z)
print(y+"hello")

def list_2_string(p):
    x=""
    for i in range(len(p)):
        x=x+str(p[i])
    return x
    
def string_2(p):
    x="["
    for i in range(len(p)):
        x=x+str(p[i])
        if i!=len(p)-1:
            x=x+","
    x=x+"]"
    return x
print(string_2([1,2,3]))