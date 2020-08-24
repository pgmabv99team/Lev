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
        g.base = "-"
        g.trail = "x"
        g.tl = 4
        g.avatar = 0
        g.x = util.make_array(g.imax, g.jmax, g.base)

        g.i = 0
        g.j = 0

        g.hist = []
        g.nmoves = 0
        g.step()

    @staticmethod
    def clear():
        irows = 0

        nrows = len(g.x)
        ncols = len(g.x[0])
        while irows < nrows:
            icols = 0
            while icols < ncols:
                g.x[irows][icols] = g.base
                icols += 1
            irows += 1

    @staticmethod
    def step():
        g.nmoves += 1

        pos = {}
        pos["rownum"] = g.i
        pos["colnum"] = g.j
        pos["trail"] = g.trail
        pos["avatar"]=g.avatar
        g.hist.append(pos)

    @staticmethod
    def render():
        start_time = time.time()

        g.clear()
        l = len(g.hist)
        # add trail

        high = len(g.hist)
        low = 0
        if high >= g.tl:
            low = high-g.tl
        for k in range(low, high):

            print(g.hist[k])
            i2 = g.hist[k]["rownum"]
            j2 = g.hist[k]["colnum"]
            g.x[i2][j2] = g.hist[k]["trail"]

        # add avatar
        g.i=g.hist[high-1]["rownum"]
        g.j=g.hist[high-1]["colnum"]
        g.avatar=g.hist[high-1]["avatar"]
        g.x[g.i][g.j] = g.avatar
        print(pandas.DataFrame(g.x))
        print(time.time()-start_time)

    @staticmethod
    def run():

        while True:

            g.render()

            print("enter command===========")
            command = input().lower().strip()

            pos = {}

            if command == "a":
                if g.j == 0:
                    print("You have reached the boundary-", g.j)
                    g.j = g.jmax-1

                else:
                    g.j = g.j-1
                g.step()

            elif command == "d":
                if g.j == g.jmax-1:
                    print("You have reached the boundary-", g.j)
                    g.j = 0
                else:
                    g.j = g.j+1
                g.step()

            elif command == "s":
                if g.i == g.imax-1:
                    print("You have reached the boundary", g.i)
                    g.i = 0
                else:
                    g.i = g.i+1
                g.step()

            elif command == "w":
                if g.i == 0:
                    print("You have reached the boundary", g.i)
                    g.i = g.imax-1
                else:
                    g.i = g.i-1
                g.step()

            elif command == "r":
                inew = random.randint(0, g.imax-1)
                jnew = random.randint(0, g.jmax-1)
                g.i = inew
                g.j = jnew
                g.step()

            elif command == "new":
                print("Enter new  avatar")
                g.avatar = input()
                g.step()

            elif command == "trail":
                print("Enter new  trail symbol")
                g.trail = input()

            elif command == "trail_off":
                print("Turning off  trail")
                g.trail = g.base

            elif command == "u":
                if len(g.hist) > 0:
                    g.hist.pop()
                else:
                    print("ERR:Cannot undo")

            elif command == "reset":
                
                v2=input("Enter 2 Dimensions ").split()
                
                if len(v2)>2 or len(v2)<1:
                    print("ERR: Number of Dimensions Expected 2 or 1. Given",len(v2))
                    continue
                
                g.imax =int(v2[0])
                if len(v2)==1:
                    print("WRN: Using 1 Number for 2 Dimensions")
                    g.jmax=int(v2[0])
                else:
                    g.jmax=int(v2[1])
                g.init()

            elif command == "stop":
                print("You have made", g.nmoves, "moves")
                break

            else:
                # print("Incorrect command... gm-destruct sequence initiated")
                # print("To survive, please re-enter the command")
                print("ERROR: You have pressed", command,
                      "Available commands are w, a, s, d, new")
                continue


# end of class
g.imax = 5
g.jmax = 5
g.init()
g.run()
