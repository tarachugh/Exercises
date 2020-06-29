# Code your solution here
def total(l):
    result=0
    for i in l:
        result+=i
    return result

l=[10, 20, 30, 40, 50, 60]
result=total(l)
print(result)