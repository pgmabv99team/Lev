def add_elements(p,n):
    pl=len(p)
    i=0
    y=[]
    z=[]
    while i<pl:
        if i<n:
            i2=0
        else:
            i2=i-n
        mysum=0
        print("working on i",i)
        
        while i2<=i:
            print("adding",p[i2],i2)
            mysum=mysum+p[i2]
            i2 +=1
        y.append(mysum)
        print(mysum)  
        if i>=n:
            ave=mysum/(n+1)
        else:
            ave=mysum/(i+1)
        z.append(ave)
        i +=1
    
    print("first list",x)
    print("average list",z)
    print("final list",y)

    yl=len(y)
x=[0,0,10,50,100,200,210,198,150,200,200,121,86,50]

add_elements(x,2)
        