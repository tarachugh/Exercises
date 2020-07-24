# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest 
    def __str__(self):
        if self.rest:
            return f'{self.first}, {self.rest}'
        else:
            return str(self.first)

# Write a function named reverse that consumes a LinkedList ll and returns a LinkedList with all the elements reversed
# reverse(Node(1, Node(2, Node(3, None)))) -> Node(3, Node(2, Node(1, None)))

def reverse(ll):
    prev=None
    curr=ll
    upcoming=None
    while curr!=None:
        upcoming=curr.rest
        curr.rest=prev
        prev=curr
        curr=upcoming
    # ll.first=prev
    return prev




ll=reverse(Node(1, Node(2, Node(3, Node(4, Node(5, None))))))
# print(ll.first)
# print(ll.rest.first)
# print(ll.rest.rest.first)
# print(ll.rest.rest.rest.first)

# n1=Node(1)
# n2=Node(2)
# n3=Node(3)
# n4=Node(4)
# n1.rest=n2
# n2.rest=n3
# n3.rest=n4
# llist=n1l

print(ll)