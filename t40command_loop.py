# command loop 
import math
import util

def Lev_prompt_numeric():
    poperand=input()
    if poperand.isdigit()==False:
        print("non-numeric poperand... self-destruct sequence initiated")
        print("To survive, please re-enter the command")
        poperand2=None
        return poperand2
    else:
        poperand2=int(poperand)
        return poperand2

def Lev_prompt_string():
    
    operand=input()
    if len(operand)==0:
        print("Empty operand... self-destruct sequence initiated")
        print("To survive, please re-enter the command")
        operand2=None
        return operand2
    else:       
        operand2=str(operand)
        return operand2







while True:
    print("enter command===========")
    command=str(input()) 
    print("you just entered a command")
    if command =="p10":
        print("enter operand to raise your number to the tenth power")
        operand=Lev_prompt_numeric()
        if operand==None:
            continue
        print(operand**10)
    elif command=="sqrt":
        print("enter operand to find square root")
        operand=Lev_prompt_numeric()
        if operand==None:
            continue
        print(math.sqrt(operand))
    elif command=="divide!":
        print("enter operand to find your number divided by 10,000")
        operand=Lev_prompt_numeric()
        if operand==None:
            continue
        print(operand/10000)
    elif command=="echo":
        print("enter word to have it echoed (wink)")
        operand=Lev_prompt_string()
        if operand == None:
            continue
        to_add="is an idot".upper()
        print(operand.upper(),to_add)
    elif command=="Do it":
        print("enter word to have fun")
        operand="https://www.youtube.com/watch?v=FJt_JdFwLw0"
        print(operand)
    elif command=="top":
        print("enter file name for analysis")
        operand=Lev_prompt_string()
        if operand == None:
            continue
        util.print_top_words(operand)

        
            
    else:
        print("Incorrect command... self-destruct sequence initiated")
        print("To survive, please re-enter the command")
        continue
    
    # output 
    



