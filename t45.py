# birb_list=[]
# for i in range(10):
#     birb={}
#     birb["time"]=i
#     if i%3==0:
#         birb["room"]="living"
#     elif i%3==1:
#         birb["room"]="kitchen"
#     else:
#         birb["room"]="bedroom"
#     if i%2==1:
#         birb["sound"]="SQUAWK"
#     birb_list.append(birb)


# i=0
# while i<=len(birb_list)-1:
#     if birb_list[i]["room"]=="kitchen":
#         birb_list[i]["action"]="poop"
#     print(birb_list[i])
#     i=i+1
def print_list(birb_list):
    i=0
    while i<=len(birb_list)-1:
        print(birb_list[i])
        i=i+1



birb_list=[]
while True:
    command=input().lower().strip()
    birb={}
    if command=="k":
        birb["room"]="kitchen"
        birb_list.append(birb)

    elif command=="l":
        birb["room"]="living"
        birb_list.append(birb)
    
    elif command=="b":
        birb["room"]="bedroom"
        birb_list.append(birb)

    elif command=="rem":
        v=int(input("Enter number "))
        if v>=len(birb_list):
            print("Err: Out of Range")
            continue
        birb_list.pop(v)
        

    
    else:
        print("bad")
        continue
    print_list(birb_list)
