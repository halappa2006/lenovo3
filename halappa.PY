s=[]
def push():
    if len(s)==size:
        print("stack is full")
    else:
        item=input("enter the element:")
        s.append(item)
def pop():
    if(len(s)==0):
        print("stack is empty")
    else:
        item=s[-1]
        del(s[-1])
        print("the deleted element is:",item)
def display():
    size=len(s)
    if(size==0):
        print("stack is empty")
    else:
        for i in reversed(s):
            print(i)
size=int(input("enter the size of stack:"))
while(True):
    choice=int(input("1-PUSH 2-POP 3- DISPLAY 4-EXIT Enter your choice:"))
    if(choice==1):
        push()
    elif(choice==2):
        pop()
    elif(choice==3):
        display()
    else:
        break