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