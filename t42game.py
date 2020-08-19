# command loop
import math
import util
import numpy
import pandas
import winsound
import random
import time

class g:

    @staticmethod
    def init():

        # g.imax = 5
        # g.jmax = 5
        g.base = "-"
        g.x = util.make_array(g.imax, g.jmax, g.base)

        g.avatar = 0
        g.i = 0
        g.j = 0
        g.x[g.i][g.j] = g.avatar

        print(pandas.DataFrame(g.x))
        g.trail = "x"

    @staticmethod
    def run():
        nmoves = 0
        while True:

            print("enter command===========")
            command = input().lower().strip()
            start_time = time.time()
            
            
            print("you just entered a command")

            if command == "a":
                
                if g.j == 0:
                    print("You have reached the boundary-", g.j)
                    util.swap_in_row(g.x, g.i, 0, g.jmax-1)
                    g.x[g.i][g.j] = g.trail
                    g.j = g.jmax-1

                else:
                    util.swap_in_row(g.x, g.i, g.j, g.j-1)
                    g.x[g.i][g.j] = g.trail
                    g.j = g.j-1
                nmoves += 1
                
            elif command == "d":
                if g.j == g.jmax-1:
                    print("You have reached the boundary-", g.j)
                    util.swap_in_row(g.x, g.i, g.jmax-1, 0)
                    g.x[g.i][g.j] = g.trail
                    g.j = 0
                else:
                    util.swap_in_row(g.x, g.i, g.j, g.j+1)
                    g.x[g.i][g.j] = g.trail
                    g.j = g.j+1
                nmoves += 1

            elif command == "s":

                if g.i == g.imax-1:
                    print("You have reached the boundary", g.i)
                    util.swap_in_column(g.x, g.j, g.imax-1, 0)
                    g.x[g.i][g.j] = g.trail
                    g.i = 0
                else:
                    util.swap_in_column(g.x, g.j, g.i, g.i+1)
                    g.x[g.i][g.j] = g.trail
                    g.i = g.i+1
                nmoves += 1

            elif command == "w":
                if g.i == 0:
                    print("You have reached the boundary", g.i)
                    util.swap_in_column(g.x, g.j, 0, g.imax-1)
                    g.x[g.i][g.j] = g.trail
                    g.i = g.imax-1
                else:
                    util.swap_in_column(g.x, g.j, g.i, g.i-1)
                    g.x[g.i][g.j] = g.trail
                    g.i = g.i-1
                nmoves += 1

            elif command == "new":
                print("Enter new  avatar")
                g.avatar = input()
                g.x[g.i][g.j] = g.avatar

            elif command == "trail":
                print("Enter new  trail symbol")
                g.trail = input()

            elif command == "trail_off":
                print("Turning off  trail")
                g.trail = g.base

            elif command=="reset":
                print("Resetting game")
                g.imax=int(input())
                g.jmax=int(input())
                g.init()            
            
            elif command=="r":
             
                inew=random.randint(0,g.imax-1)
                jnew=random.randint(0,g.jmax-1)

                print(inew,jnew)

                a=g.x[g.i][g.j]
                g.x[g.i][g.j]=g.x[inew][jnew]
                g.x[inew][jnew]=a
                
                g.x[g.i][g.j]=g.trail
                g.i=inew
                g.j=jnew

                


            elif command == "stop":
                print("You have made", nmoves, "moves")
                break

            else:
                # print("Incorrect command... gm-destruct sequence initiated")
                # print("To survive, please re-enter the command")
                print("ERROR: You have pressed", command,
                      "Available commands are w, a, s, d, new")
                continue

            print(pandas.DataFrame(g.x))
            print(time.time()-start_time)

# end of class
g.imax=5
g.jmax=5
g.init()
g.run()
