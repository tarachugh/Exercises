# Code your solution here
def fact(n):
    i=1
    result=1
    while i<=n:
        result=result*i
        i+=1
    return result

n=input()
result=fact(n)
print(result)