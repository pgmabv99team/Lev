# class
class person:
    def __init__(self, pname, page, pgender, phcolor):

        self.name = pname

        # if page > 100:
        #     page = None
        self.age = page

        self.gender = pgender.upper()

        if page != None:
            self.yob = 2020-self.age
        else:
            self.yob = None

        if phcolor == "":
            phcolor = "bald"
        self.hcolor = phcolor
    
    def GoodlyOrUngoodly(self):
        if self.age>=35 or self.hcolor=="bald":
            return "bad"
        else:
            return "good"

    def MakeBald(self):
        self.hcolor="bald"


people = []
x = person("Shura", 40, "female", "brown")
people.append(x)
x = person("Whiskey", 1, "unknown", "multi")
people.append(x)
x = person("Papa", 60, "male", "")
people.append(x)
x=person("Lev",12,"male","straw")
people.append(x)
x=person("Whiskey",10000,"LGBTQ","green")
people.append(x)
peoplel = len(people)



# mymax=people[i].age
# while i < peoplel:
#     print(people[i].name, people[i].age, people[i].gender,
#           people[i].yob, people[i].hcolor)
#     if people[i].age>mymax:
#         mymax=people[i].age
#     i = i+1
# print(mymax)
# i = 0

# while i<peoplel:
#     print(people[i].name,people[i].GoodlyOrUngoodly())
#     if people[i].name=="Whiskey":
#         people[i].MakeBald()
#     print(people[i].hcolor)
#     i=i+1

for x in people:
    print(x.age)