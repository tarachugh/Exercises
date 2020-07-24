# class Node:
#     # first: int
#     # rest: LinkedList
#     def __init__(self, first, rest=None):
#         self.first=first
#         self.rest=rest

# class Stack:
#     def __init__(self, head=None):
#         self.head=head
        

#     def check_stack_empty(self):
#         if self.head==None:
#             return True
#         return False

# node_1=Node(1)
# stack_1= Stack()
# print(stack_1.check_stack_empty())

# code written so pytest works        

def check_stack_empty(stack):
    if stack==[]:
        return True
    return False

stack_1=[]
print(check_stack_empty(stack_1))