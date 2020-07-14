# class
class person:
    def __init__(self, pname, page, pgender, phcolor):

        self.name = pname

        if page > 100:
            page = None
        self.age = page

        self.gender = pgender.upper()

        if page != None:
            self.yob = 2020-self.age
        else:
            self.yob = None

        if phcolor == "":
            phcolor = "bald"
        self.hcolor = phcolor


people = []
x = person("Shura", 40, "female", "brown")
people.append(x)
x = person("Whiskey", 1, "unknown", "multi")
people.append(x)
x = person("Papa", 60, "male", "")
people.append(x)
x=person("Lev",12,"male","straw")
peoplel = len(people)
i = 0
mymax=people[i].age
while i < peoplel:
    print(people[i].name, people[i].age, people[i].gender,
          people[i].yob, people[i].hcolor)
    if people[i].age>mymax:
        mymax=people[i].age
    i = i+1
print(mymax)
