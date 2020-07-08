# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function named concatenate that consumes 2 LinkedLists ll1 and ll2. The function returns a LinkedList with all elements of ll1 followed by all elements in ll2.
# ie. concatenate(Node(1, Node(2, None)), Node(3, Node(4, None))) -> Node(1, Node(2, Node(3, Node(4, None))))

def concatenate(ll1, ll2):
    if ll1==None:
        new= ll2
    elif ll2==None:
        new= ll1
    elif ll1.rest==None:
        new= Node(ll1.first, ll2)
    else:
        new=Node(ll1.first)
        new.rest=concatenate(ll1.rest, ll2)
    return new

# a=Node(1)
# a.rest=2

# d1=Node(6)
# c1=Node(5, d1)
# b1=Node(4,c1)
# a1=Node(3, b1)


# result=concatenate(a, a1)
# # node=result.first
# # while node:
# #     print(node.first)
# #     node=node.rest

node=concatenate(Node(1, Node(2, None)), Node(3, Node(4, None)))

print(node.first)
print(node.rest.first)
print(node.rest.rest.first)
print(node.rest.rest.rest.first)
# while node:
#     print(node)
#     node=node.rest