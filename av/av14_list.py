class node:

    def __init__(self,pv):
        self.v=pv
        self.next=None

    def list_2_num(self):
        if self.next==None :
            return self.v, 1
        else :
            next=self.next
            num,pos=next.list_2_num()
            numa=self.v*(10**pos)
            pos2=pos+1
            print(pos2,numa)
            num2=num+numa
            return num2, pos2

            

class slist:
    def __init__(self):
        self.first=None

    def add_f(self,node):
        node.next=self.first
        self.first=node


    def show(self):
        node=self.first
        while (node!=None):
            print(node.v,end="->")
            node=node.next
        print()

    def list_2_num(self):
        node=self.first
        num,pos=node.list_2_num()
        print("final", num, pos)



s1=slist()
s1.add_f(node(1))
s1.add_f(node(2))
s1.add_f(node(3))
s1.show()
s1.list_2_num()

s2=slist()
s2.add_f(node(0))
s2.add_f(node(0))
s2.add_f(node(1))
s2.show()
s2.list_2_num()