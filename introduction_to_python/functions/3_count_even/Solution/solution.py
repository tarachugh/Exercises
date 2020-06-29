# Code your solution here
def count_even(**kwargs):
    count=0
    for i in kwargs.values():
        if i%2==0:
            count+=1
    return count
    
result=count_even(key1=1, key2=2, key3=9, key4=9)
print(result)