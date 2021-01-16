def dominator(p):
    dict={}
    for i in range(len(p)):
        if p[i] not in dict:
            dict[p[i]]=1

        else:
            dict[p[i]] +=1
        if dict[p[i]]>len(p)/2:
            return p[i]
    return None

def solution(p):
    pl=len(p)
    equi_num=0
    for i in range(pl):
        begin=p[0:i]
        end=p[i:]
        # print(begin,end)
        dom_begin=dominator(begin)
        dom_end=dominator(end)
        if dom_begin==dom_end and dom_begin!=None:
            equi_num +=1
    return equi_num
# old version ends











def d_build(p):
    dict={}
    for i in range(len(p)):
        if p[i] not in dict:
            dict[p[i]]=1

        else:
            dict[p[i]] +=1
    return dict

# return key which contains the maximum value.
def d_max(p):
    max_count=0
    max_key=None
    for key in p:
        if p[key]>max_count:
            max_count=p[key]
            max_key=key
    return max_key,max_count

def solution(p):
    pl=len(p)
    equi_num=0
    d_begin=d_build(p[0:0])
    d_end=d_build(p[0:])
    print(d_begin,d_end)
    for i in range(pl):
        v=p[i]
        d_end[v] -=1
        if v in d_begin:
            d_begin[v]=d_begin[v]+1
        else:
            d_begin[v]=1
        # print(i,v,d_begin,d_end)
        res=d_max(d_begin)
        max_key_begin=res[0]
        max_count_begin=res[1]
        res=d_max(d_end)
        max_key_end=res[0]
        max_count_end=res[1]
        if max_count_begin>(i+1)/2 and max_count_end>(pl-i-1)/2:
            if max_key_begin==max_key_end:
                equi_num +=1

    return equi_num

print(solution([4,3,4,4,4,2]))