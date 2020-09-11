def add_elements(p,n,k):
    pl=len(p)
    i=0
    y=[]
    z=[]
    while i<pl:
        low=max(0,i-n)
        high=min(pl-1,i+k)
        count=high-low+1
        print(i,low,high,count)

        mysum=0
        # i2=low       
        # while i2<=high:
        #     mysum=mysum+p[i2]
        #     i2 +=1
        for i2 in range(low,high+1,1):
            mysum=mysum+p[i2]
        y.append(mysum)
        ave=mysum/count
        
        z.append(ave)
        i +=1
    
    print("first list",x)
    print("average list",z)
    print("final list",y)

    yl=len(y)
x=[0,0,10,50,100,200,210,198,150,200,200,121,86,50]
x=[0,1,2,3,4,5,6]

add_elements(x,2,1)
        