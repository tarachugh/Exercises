# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest 

# Write a function named reverse that consumes a LinkedList ll and returns a LinkedList with all the elements reversed
# reverse(Node(1, Node(2, Node(3, None)))) -> Node(3, Node(2, Node(1, None)))

def reverse(ll):
    prev=None
    curr=ll.first
    while curr!=None:
        upcoming=ll.rest
        ll.rest=prev
        prev=curr
        curr=upcoming
    ll.first=prev
    return ll




ll=(Node(1, Node(2, Node(3, Node(4, Node(5, None))))))
reverse(ll)
print(ll.first)
print(ll.rest.first)
print(ll.rest.rest.first)
print(ll.rest.rest.rest.first)
print(ll.rest.rest.rest.rest.first)

