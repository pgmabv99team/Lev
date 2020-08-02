# command loop 
import math
while True:
    print("enter command")
    command=str(input()) 
    print("you just entered a command")
    if command =="p10":
        
        print("enter operand")
        operand = input()
        if operand.isdigit()==False:
            print("non-numeric operand... self-destruct sequence initiated")
            print("To survive, please re-enter the command")
            continue
        operand2=int(operand)
        print("result",operand2**10)
    elif command=="sqrt":
        print("enter operand to find square root")
        operand=input()
        if operand.isdigit()==False:
            print("non-numeric operand... self-destruct sequence initiated")
            print("To survive, please re-enter the command")
            continue
        operand2=int(operand)
        print(math.sqrt(operand2))
    elif command=="divide!":
        print("enter operand to find your number divided by 10,000")
        operand=input()
        if operand.isdigit()==False:
            print("non-numeric operand... self-destruct sequence initiated")
            print("To survive, please re-enter the command")
            continue
        operand2=int(operand)
        print(operand2/10000)
    elif command=="echo":
        print("enter word to have it echoed (wink)")
        operand=input()
        if len(operand)==0:
            print("Empty operand... self-destruct sequence initiated")
            print("To survive, please re-enter the command")
            continue
        operand2=str(operand)
        res="is an idot".upper()
        print(operand2.upper(),res)
    else:
        print("Incorrect command... self-destruct sequence initiated")
        print("To survive, please re-enter the command")
        continue
    
    # output 
    
    
    