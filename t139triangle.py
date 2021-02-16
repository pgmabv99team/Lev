


def solution2(a):
    al = len(a)
    
    for p in range(al):
        for q in range(p+1, al):
            for r in range(q+1, al):

                triangle=is_triangle(p,q,r,a)
                
                if triangle == True:
                    return 1
    return 0

def is_triangle(p, q, r, a):
    if a[p]+a[q] > a[r] and \
        a[q]+a[r] > a[p] and \
            a[r]+a[p] > a[q]:
        triangle = True
    else:
        triangle = False
    # print(p,q,r,"values",a[p],a[q],a[r],triangle)
    return triangle

def solution(a):
    al = len(a)
    a.sort(reverse=True)
    # print(a)
    for p in range(al-2):
        q=p+1
        r=q+1
        if is_triangle(p,q,r,a)==True:
            return 1
    return 0




print(solution([3, 5, 2, 9, 1,4]))
