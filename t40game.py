# command loop 
import math
import util






x=[0,0,0,1,0,0]
i=3
xl=len(x)

while True:
    print(x)
    print("enter command===========")
    command=str(input()) 
    print("you just entered a command")
    if command=="a":
        if i==0:
            print("You have reached the boundary-",i)
            a=x[xl-1]
            x[xl-1]=x[0]
            x[0]=a
            i=xl-1

        else:
            a=x[i]
            x[i]=x[i-1]
            x[i-1]=a
            print(x)
            i=i-1
        
            



    elif command=="d":
        if i==xl-1:
            print("You have reached the boundary-",i)
            a=x[xl-1]
            x[xl-1]=x[0]
            x[0]=a
            i=0

        else:
            a=x[i]
            x[i]=x[i+1]
            x[i+1]=a
            print(x)        
            i=i+1

    
            
    else:
        print("Incorrect command... self-destruct sequence initiated")
        print("To survive, please re-enter the command")
        continue

    if i==2:
        print("(._.)")
        for j in range(xl):
            if x[j]==1:
                x[j]=0
            else:
                x[j]=1

    
    # output 
    



