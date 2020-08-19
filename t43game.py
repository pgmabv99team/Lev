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
        g.avatar = 0
        g.x = util.make_array(g.imax, g.jmax, g.base)

        g.i = 0
        g.j = 0

        g.list_pos = []
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
        pos["i"] = g.i
        pos["j"] = g.j
        pos["trail"] = g.trail
        g.list_pos.append(pos)
    @staticmethod
    def render():
        g.clear()
    
            # add trail
        for k in range(len(g.list_pos)):
            print(g.list_pos[k])
            i2 = g.list_pos[k]["i"]
            j2 = g.list_pos[k]["j"]
            print(i2, j2)
            g.x[i2][j2] = g.list_pos[k]["trail"]

        # add avatar
        g.x[g.i][g.j] = g.avatar
        print(pandas.DataFrame(g.x))
    @staticmethod
    def run():

        while True:
            pos = {}
            start_time = time.time()
            g.render()
            print(time.time()-start_time)
            print("enter command===========")
            command = input().lower().strip()
            
            pos = {}

            print("you just entered a command")

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

            elif command == "new":
                print("Enter new  avatar")
                g.avatar = input()

            elif command == "trail":
                print("Enter new  trail symbol")
                g.trail = input()

            elif command == "trail_off":
                print("Turning off  trail")
                g.trail = g.base

            elif command == "reset":
                print("Resetting game")
                g.imax = int(input())
                g.jmax = int(input())
                g.init()

            elif command == "r":

                inew = random.randint(0, g.imax-1)
                jnew = random.randint(0, g.jmax-1)
                g.i = inew
                g.j = jnew

                g.step()

            elif command == "stop":
                print("You have made", nmoves, "moves")
                break

            else:
                # print("Incorrect command... gm-destruct sequence initiated")
                # print("To survive, please re-enter the command")
                print("ERROR: You have pressed", command,
                      "Available commands are w, a, s, d, new")
                continue

            print(time.time()-start_time)


# end of class
g.imax = 5
g.jmax = 5
g.init()
g.run()
