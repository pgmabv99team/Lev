import math
def count_in2(num):
    print(num)
    mysum=0
    while num>0:
        dig=num%10
        rest=math.floor(num/10)
        print(dig,rest)
        num=rest
        mysum +=dig
    return mysum


print(count_in2(1234))