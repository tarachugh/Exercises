# Code your solution here
def shut_down(x):
    # if x.lower()=="true":
    if x==True:
        data= "SHUTDOWN"
    # elif x.lower()=="false":
    elif x==False:
        data="SHUTDOWN ABORTED"
    else:
        data= "X NOT VALID"
    return data

x=input()
result=shut_down(x)
print(result)
