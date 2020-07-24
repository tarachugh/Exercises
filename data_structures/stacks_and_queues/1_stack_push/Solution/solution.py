# class Node:
#     def __init__(self, first, rest=None):
#         self.first=first
#         self.rest=rest

# class Stack:
#     def __init__(self, head=None):
#         self.head=head
        

# def push(stack_a):
#     head_new=Node("Python")
#     head_new.rest=stack_a.head
#     stack_a.head=head_new

# stack_a=Stack(Node("C", Node("C++", Node("Java", None))))
# push(stack_a)
# print(stack_a.head.first)





# code modified so that pytest works:

# def push(stack_a):
#     stack_a.append("Python")
#     return stack_a

# stack_a=["C", "Perl", "C++", "Java"]
# result=push(stack_a)
# print(result)






# code modified so that pytest works, round 2

def push(stack_a):
    stack_a.append("4")
    return stack_a

stack_a=["1", "2", "3"]
result=push(stack_a)
print(result)