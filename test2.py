x=[1,2]
def add_10(p):
    pl=len(p)
    for i in range(pl):
        p[i]=p[i]+10
    return "done"

res=add_10(x)
print(add_10(x))
print(x)