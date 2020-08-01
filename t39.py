# test for merge lists
import util

# x=[-12,23,42,563]
# y=[23,12,1231231,2322323,4545]
# util.list_sort(x)
# util.list_sort(y)

# zp=util.merge_lists(x,y)
# print(zp)

x=[]
y=[23,12,1231231,2322323,4545]
util.list_sort(x)
util.list_sort(y)

zp=util.merge_lists(x,y)
print(zp)