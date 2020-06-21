#bubble sort
x = [23, 65, 10000000000, 54, 877, 90909, 1]
xl = len(x)


def swaap(p, ip):
    print("Swaap pair before", p[ip], p[ip+1])
    h = p[ip]
    p[ip] = p[ip+1]
    p[ip+1] = h
    print("Swaap pair after", p[ip], p[ip+1])


def iteration():


    i = 0
    while i < xl-1:
        print("element", i, x[i], x[i+1])
        if x[i] > x[i+1]:
            swaap(x, i)
        i = i+1
    print(x)


J=0
while J<xl-1:
    iteration()
    J=J+1
print("Final version of x array",x)

