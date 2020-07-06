from array import *
array_num = array('i', [1, 2,3, 2, 1, 0])
element = int(input("input an element in the array"))
count = 0
for i in array_num:
    if i == element:
        count +=1
print(count) 