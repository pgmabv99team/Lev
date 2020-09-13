class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.hair_color="black"
        self.children=[]
        print("__init__ called",self,self.name,self.age)
        
    def info(self,depth):
        temp="++"
        
        print(depth*temp,self.name,self.age,self.hair_color)

    def set_hair_color(self,hair):
        self.hair_color=hair
    
    def add_child(self,node):
        print("add_child called",node.name,"to",self.name)
        self.children.append(node)

class family_t:
    def __init__(self,family_name):
        self.family_name=family_name
        p_n=Person("Nonchik",87)
        self.family_root=p_n

        p_k=Person("Katya",60)
        p_n.add_child(p_k)
        p_g=Person("Genya",66)
        p_n.add_child(p_g)

        p_s=Person("Shura",41)
        p_g.add_child(p_s)

        p_li=Person("Liuba",22)
        p_k.add_child(p_li)

        p_ko=Person("Kostia",46)
        p_g.add_child(p_ko)

        p_l=Person("Liova",12)
        p_s.add_child(p_l)

        p_b=Person("Birb",1.6)
        p_l.add_child(p_b)

        p_gr=Person("Grisha",18)
        p_ko.add_child(p_gr)


    def set_hair_color(self,person):
        if person.age>45:
            person.set_hair_color("Grey")
        for i in range(len(person.children)):
            self.set_hair_color(person.children[i])


    def info(self,person,depth):
        # print("enter")
        person.info(depth)
        for i in range(len(person.children)):
            # person.children[i].info()
            self.info(person.children[i],depth+1)

        # print("exit")



family=family_t("Clan Walrus") 

family.set_hair_color(family.family_root)
family.info(family.family_root,0)


