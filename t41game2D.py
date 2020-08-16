# command loop 
import math
import util
import numpy
import pandas





x=[[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
print(pandas.DataFrame(x))
i=0
j=0
xl=len(x)
imax=len(x)
jmax=len(x[0])
# print(imax,jmax)


while True:
   
    print("enter command===========")
    command=str(input()) 
    print("you just entered a command")
    if command=="a":
        if j==0:
            print("You have reached the boundary-",j)
            util.swap_in_row(x,i,jmax-1,0)
            j=jmax-1
        else:
            util.swap_in_row(x,i,j,j-1)
            j=j-1
        
    elif command=="d":
        if j==jmax-1:
            print("You have reached the boundary-",j)
            util.swap_in_row(x,i,0,jmax-1)
            j=0
        else:
            util.swap_in_row(x,i,j,j+1)
            j=j+1     

    elif command=="s":
        
        if i==imax-1:
            print("You have reached the boundary",i)
            util.swap_in_column(x,j,0,imax-1)
            i=0
        else:
            util.swap_in_column(x,j,i,i+1)
            i=i+1

    elif command=="w":
        if i==0:
            print("You have reached the boundary",i)
            util.swap_in_column(x,j,0,imax-1)
            i=0
        else:
            util.swap_in_column(x,j,i,i-1)
            i=i-1
    elif command=="new":
        print("Enter new avatar")
        avatar=input()
        x[i][j]=avatar

     
    else:
        # print("Incorrect command... self-destruct sequence initiated")
        # print("To survive, please re-enter the command")
        print("ERROR: You have pressed",command,"Available commands are w, a, s, d, new")
        continue
    
    print(pandas.DataFrame(x))

    # if i==2:
    #     print("(._.)")
    #     for j in range(xl):
    #         if x[j]==1:
    #             x[j]=0
    #         else:
    #             x[j]=1

    
    # end of loop 
    



