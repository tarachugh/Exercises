class Stack:
    def __init__(self):
        self.values = []
    def empty(self):
        if self.values==[]:
            return True
        return False
        
    def push(self, value_to_add):
        self.values.append(value_to_add)

    def pop(self):
        return self.values.pop()

class Queue:
    def __init__(self):
        self.values = []

    def  empty(self):
        if self.values==[]:
            return True
        return False

    def enqueue(self, value_to_add):
        self.values.append(value_to_add)

    def dequeue(self):
        ret=self.values[0]
        self.values=self.values[1:]
        return ret


def Reverse(stack, queue):
    while queue.empty()!=False:
        stack.push(queue.dequeue)
    while queue.empty()!=False:
        queue.enqueue(stack.pop())
    return queue
        
St = Stack() 
Qu = Queue()
Qu.enqueue(1)
Qu.enqueue(2)
Qu.enqueue(3)
Qu.enqueue(4)
Qu.enqueue(5)
QuNew= Reverse(St, Qu)
print(QuNew.values)