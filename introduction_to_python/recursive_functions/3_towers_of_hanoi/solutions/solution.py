# Write your solution here
"""
make stack of n-1 disks on aux_rod
first disk moves to to_rod with even n, first disk moves to aux_rod on odd n
base case: n=1: return 1
""" 

#this one was done the way the problem told it to be done

def tower_of_hanoi(n, from_rod="from", to_rod="to", aux_rod="aux"):
    if n==1:
        return 1
    return tower_of_hanoi(n-1, from_rod, aux_rod,to_rod)+1+tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)
    #making stack of n-1 disks onto the aux rod from the from_rod
    #the plus 1 in the middle is moving the nth disk to the to_rod from the from_rod 
    #then moving the stack of n-1 disks from the aux_rod to the to_rod
print(tower_of_hanoi(4, "source", "to", "aux"))


# #modified so pytest works
# def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
#     if n==1:
#         return 1
#     return tower_of_hanoi(n-1)+1+tower_of_hanoi(n-1)
    