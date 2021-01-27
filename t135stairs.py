def stairs(n,slist,mlist,mysummary):
    if n>=1:
        slist.append(1)
        stairs(n-1,slist,mlist,mysummary)
        slist.pop()
    if n>=2:
        slist.append(2)
        stairs(n-2,slist,mlist,mysummary)
        slist.pop()
    if n==0:
        slist2=slist.copy()
        mlist.append(slist2)
        # print("slist=",slist,"mlist=",mlist)

        mysummary.count +=1
        print(mysummary.count)
    


slist=[]
mlist=[]
class summary:
    count=0
mysummary=summary()
stairs(3,slist,mlist,mysummary)
print(mysummary.count)