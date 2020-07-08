# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function named create_list that consumes a number n and returns a LinkedList of 1,2,..,n 
# create_list(3) -> Node(1, Node(2, Node(3, None)))
def create_list(n):
    return _create_list(n,1)

def _create_list(n, index):
    if index<=n:
        new=Node(index)
        new.rest=_create_list(n, index+1)
        return new
    return None

node=create_list(3)

print(node.first)
print(node.rest.first)
print(node.rest.rest.first)

