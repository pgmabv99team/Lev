# factorial
def MyFactorial(nn):
    f = 1
    i = 1
    while i <= nn:
        f = f*i
        i = i+1
    return f
x=[4,5,6,7]
xl=len(x)
i=0
while i<xl:
    factorial = MyFactorial(x[i])
    print(factorial)
    i=i+1


