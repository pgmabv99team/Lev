def in_list(p):
    if 1 in d:
        return True

def mysort(p):
    p.sort()

def in_list_man(p):
    for i in p:
        if i==1:
            return True

d=[0]*(10**8)
d[len(d)-1]=1




# timing the function
import time
start_time = time.time()
print(in_list(d))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(mysort(d))
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
print(len(d))
print("--- %s seconds ---" % (time.time() - start_time))

