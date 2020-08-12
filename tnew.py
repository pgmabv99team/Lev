import os

# with os.scandir('files') as entries:
def LevsFunction(root, level):
    level +=1
    sep=level*"+++++"
    print("enter====",sep,root,level)
    list_entries=os.scandir(root)
    fl=0
    for myentry in list_entries:
        if myentry.is_file():
            print(myentry, "is a file ", myentry.stat().st_size)
            fl=fl+myentry.stat().st_size
        else:
            print(myentry, "is a folder")
            res=LevsFunction(myentry,level)
            fl=fl+res
            print("result = ",res)
    list_entries.close()
    print("exit==== ",sep,level)
    level -=1
    print(fl)
    return fl
# entry.stat().st_size
fl=0
res=LevsFunction("filesx",0)
print("result = ",res)
