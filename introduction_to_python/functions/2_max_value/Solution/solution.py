# Code your solution here
def max_value(a,b,c):
    if a>=b and a>=c:
        result=a
    elif b>=a and b>=c:
        result=b
    else:
        result=c
    return result

a=input()
b=input()
c=input()
result=max_value(a,b,c)
print(result)
