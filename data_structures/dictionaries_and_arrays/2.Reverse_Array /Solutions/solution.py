from array import *
array_num = array('i', [1,2,3,4,5,6,7,8,9])
reverse_array = array('i')
for i in range(len(array_num)-1,-1,-1):
    reverse_array.append(array_num[i])
print(reverse_array)
