# Code your solution here
def shut_down(x):
    if x.lower()=="true":
        data= "SHUTDOWN"
    elif x.lower()=="false":
        data="SHUTDOWN ABORTED"
    else:
        data= "X NOT VALID"
    return data

x=input()
result=shut_down(x)
print(result)
