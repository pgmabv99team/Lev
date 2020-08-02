#Min and max of an array of integers
import math as m

numbers = [-45,45,34,23,12,-100]
i = 0
numbersl = len(numbers)
print(numbersl)
mymin = numbers[0]
mymax = numbers[0]
while i < numbersl:

    number = numbers[i]
    # test = numbers[i].upper()
    print("number", i, number, number, "characters")
    if number < mymin:
        mymin = number
        print("new mymin", mymin)
    else:
        print("no new mymin")
    if number > mymax:
        mymax = number
        print("new mymax", mymax)
    else:
        print("no new mymax")

    i = i+1
print("final mymin", mymin,"final mymax", mymax)
print(min(numbers))
mymin2=min(numbers)
mysquareroot=m.sqrt(35)
print(mysquareroot)