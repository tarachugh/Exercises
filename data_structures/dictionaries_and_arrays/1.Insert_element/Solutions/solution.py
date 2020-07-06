from array import array
arr = array('i', [1, 2, 3, 4, 5])
ins_pos = int(input("enter position to insert"))
ins_val = int(input("enter value to insert"))
arr.insert(ins_pos, ins_val)
print(arr)


