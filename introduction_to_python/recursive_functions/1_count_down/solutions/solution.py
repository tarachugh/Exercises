# Write your solution here
def count_down_from(num):
    if num==1:
        print(1)
    else:
        print(num)
        count_down_from(num-1)