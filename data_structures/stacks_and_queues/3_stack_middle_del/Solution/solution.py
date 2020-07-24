class Stack: 
	def __init__(self): 
		self.items = [] 
	
	def isEmpty(self): 
		return self.items == [] 
	
	def push(self, item): 
		self.items.append(item) 
	
	def pop(self): 
		return self.items.pop() 
	
	def peek(self): 
		return self.items[len(self.items)-1] 
	
	def size(self): 
		return len(self.items) 
		
def deletemid(stack, size, index_now) : 

	if (stack.isEmpty() or index_now == size) : 
		return
	
	taken_off = stack.peek() 
	stack.pop() 
	
	deletemid(stack, size, index_now+1) 
	
	if index_now != (size//2) : 
		stack.push(taken_off) 


a=Stack()
a.push('1') 
a.push('2') 
a.push('3') 
a.push('4') 
a.push('5') 
a.push('6') 
a.push('7') 

deletemid(a, a.size(), 0)
result=a.items
print(result)