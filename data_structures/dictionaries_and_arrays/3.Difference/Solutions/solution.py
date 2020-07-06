from array import array 
array_num = array('i', [7,6,5,4,3,2,1])
greatest=array_num[0]
smallest=array_num[0]
for i in array_num:
    if i>greatest:
        greatest=i
for i in array_num:
    if i<smallest:
        smallest=i
result=greatest-smallest
print(result)