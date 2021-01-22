d=[-3,2,-54,7,12,-12]
print(max(d))
# abs_max=d[0]
# for i in d:
#     if abs(i)>abs_max:
#         abs_max=abs(i)
# print(abs_max)
def my_abs(a):
    temp=abs(a)
    if a%3==0:
        temp=-99
    return temp

print(max(d,key=my_abs))
print(max(d,key=lambda x: -99 if x % 3 == 0 else abs(x)))
# lambda x: True if x % 2 == 0 else False
d="birdaabbbbb"
