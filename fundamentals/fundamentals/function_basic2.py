#1
def countdown(x):
    l=[x]
    for i in range(x-1,0,-1):
        l.append(i)
    print(l)
x=int(input("donner un nombre"))
countdown(x)
#2
def Print_and_Return(a,b):
    print(a)
    return(b)
Print_and_Return(1,2)
#3
def First_Plus_Length(l):
    print (l[0]+len(l))
l=[1,2,3,4,5]
First_Plus_Length(l)
def Values_Greater_than_Second(l):
    if(len(l)<2):
        print(False)
    else:
        list2=[]
        for i in range(len(l)):
            if (l[i]>l[1]):
                list2.append (l[i])
        print(list2)
l=[5,2,3,2,1,4]
Values_Greater_than_Second(l)
def This_Length_That_Value(a,b):
    l=[]
    for i in range(a):
        l.append(b)
    print (l)
This_Length_That_Value(4,7)