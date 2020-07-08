# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function called has_cycle that consumes a LinkedList ll and returns True if ll contains a cycle and False otherwise
# x = Node(1, Node(2, x))
# has_cycle(Node(1, Node(2, None))) -> False
# has_cycle(x) -> True

# def has_cycle(ll):
#     return _has_cycle(ll, [])

# def _has_cycle(ll, already_seen):
#     current=ll
#     if ll==None:
#         return False
#     elif current in already_seen:
#         return True
#     else:
#         already_seen.append(current)
#         _has_cycle(ll.rest, already_seen)

def has_cycle(ll):
    ret=False
    if ll==None:
        return False
    skips_2=ll.first
    skips_1=ll.rest
    while skips_2!=None and skips_1!=None:
        if(skips_2==skips_1):
            ret= True
        else:
            skips_2=skips_2.rest.rest
            skips_1=skips_1.rest
    return ret





x=Node(3, Node(4, x))
y=has_cycle(Node(1, Node(2, None)))
z=has_cycle(x)
print(str(y))
print(str(z))