def coins(n,sel,mlist):
    if n>=5:
        sel.append(5)
        coins(n-5,sel,mlist)
        sel.pop()
    if n>=1:
        sel.append(1)
        coins(n-1,sel,mlist)
        sel.pop()
    if n==0:
        sel_sort=sorted(sel)
        if sel_sort not in mlist:
            mlist.append(sel_sort)
            
            print(mlist)





mlist=[]
sel=[]
print(coins(11,sel,mlist))