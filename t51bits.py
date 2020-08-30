i=1
print(format(i,'016b'))
j=5
print(format(j,'016b'))
myand=i&j
print("and",format(myand,'016b'))
myor=i|j
print("or",format(myor,'016b'))
myXOR=i^j
print("xor",format(myXOR,'016b'))
mynegative=~i
print("tilde",format(mynegative,'016b'))
print("tilde",bin(mynegative))

