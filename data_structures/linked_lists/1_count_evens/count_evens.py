# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function named count_evens that consumes a LinkedList ll and returns how many even numbers are in the list
# count_evens(Node(1, Node(2, Node(3, None)))) -> 1
count=0

def count_evens(ll):
    global count
    if ll == None:
        print ("none" +str(count))
        return 0
    elif ll.first %2==0:
        print("doing even recursion")
        count+= 1
        # print("even"+str(count))
        count_evens(ll.rest)
        # print("even recursive"+str(count))
    else:
        print("doing odd recursino")
        count_evens(ll.rest)
        # print("odd recursive"+str(count))
    return(count)


print(count_evens(Node(4, Node(2, Node(4, None)))))



"""
if there is no linked list, return 0

if the first value in linked list is even, increment count
do count evens on the next value on the list, until there is no next value, 
then return count

if the first value in the linked list is not even, 
do count evens on the next value on the list, until there is no next value,
then return count

"""