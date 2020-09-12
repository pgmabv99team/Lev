class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.hair_color="black"
        self.children=[]
        
    def info(self):
        print(self.name,self.age)

    def set_hair_color(self,hair):
        if self.age>50:
            self.hair_color="Grey"

class family_t:
    def __init__(self,family_name):
        self.family_name=family_name
        person_n=Person("Nonchik",87)
        self.family_root=person_n

        person_k=Person("Katya",60)
        person_n.children.append(person_k)
        person_g=Person("Genya",66)
        person_n.children.append(person_g)



    def info(self):
        print(self.family_name)
        self.family_root.info()
        for i in range(len(self.family_root.children)):
            self.family_root.children[i].info()



family=family_t("Clan Walrus") 

family.info()

