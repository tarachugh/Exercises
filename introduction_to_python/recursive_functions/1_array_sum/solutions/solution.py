# Write your solution here
def sum_array(num_list):
    if len(num_list)==0:
        return 0
    return num_list.pop()+sum_array(num_list)