from array import array
my_array = array('i', [1,2,3,4,5,6])
buffer_info = my_array.buffer_info()
print(buffer_info)

