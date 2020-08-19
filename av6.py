
# st_l=[]

# st={"ip":0,"jp":0,"avatar":"***"}
# st_l.append(st)
# st={"ip":1,"jp":0,"avatar":"***"}
# st_l.append(st)
# st={"ip":1,"jp":2,"avatar":"***"}
# st_l.append(st)


# print(st_l)
# print(st_l[0]["avatar"])


x=[]
a={"Name":"Lev","Age":12,"Hair":"Bald"}
x.append(a)
b={"Name":"Papa","Age":60,"Hair":"Black"}
x.append(b)
c={}
Myname="Mama"
Myage=40

c["Name"]=Myname
c["Age"]=Myage
c["Hair"]="Brown"
x.append(c)
i=0
xl=len(x)
while i<xl:
    print(x[i]["Hair"],x[i]["Age"])
    i=i+1
