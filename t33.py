# make  def function to compute the max and the min
# for 2 dimensional matrix.
# using "for" loop
#  passing lists and scalar



def MyFunc(p,n):
    nrows=len(p)
    ncols=len(p[0])

    t=[]
    for irows in range(nrows):
        for icols in range(ncols):
            t.append(p[irows][icols]*n)
    return t

def MyFuncLev(p,n):
    nrows=len(p)
    ncols=len(p[0])
    t=[]
    for irows in range(nrows):
        row=[]
        for icols in range(ncols):
            row.append(p[irows][icols]*n)
        t.append(row)
    return t

def MyFunc2(p,n):
    nrows=len(p)
    ncols=len(p[0])

    for irows in range(nrows):
        for icols in range(ncols):
           p[irows][icols]=p[irows][icols]*n

    print(p)

def MyFunc3(q,n):
    q=q*n
    print(q)

  




            



yy = [[11, 33, 45],
      [6, 7, 8],
      [456, 54, 65]]
xx = [[23, 35, 43],
      [6, 15, 8]]
# print(xx)
# print(DataFrame(xx))
res=MyFuncLev(xx,10)
print(res)

