# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function called omit_first_n that consumes a LinkedList ll and an integer n. The function returns a LinkedList with the first n elements omitted or None if n > len(ll)
# omit_first_n(Node(1, Node(2, Node(3, None))), 2) -> Node(3, None)
def omit_first_n(ll, n):
    if n==0:
        return ll
    elif ll==None:
        return None
    elif n==1:
        return ll.rest
    return omit_first_n(ll.rest, n-1)

    
node=omit_first_n(Node(1, Node(2, Node(3, Node(4, None)))), 2)
print(node.first)
print(node.rest.first)


# d1=Node(6)
# c1=Node(5, d1)
# b1=Node(4,c1)
# a1=Node(3, b1)


# result=concatenate(a, a1)
# # node=result.first
# # while node:
# #     print(node.first)
# #     node=node.rest
