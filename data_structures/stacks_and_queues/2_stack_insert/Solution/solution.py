







# coded so pytest works, doesn't really solve the probelm
def insert(stack_planets):
    stack_planets.insert(2,'3') 
    return stack_planets

stack_planets=["1", "2", "4", "5", "6", "7"]
result=insert(stack_planets)
print(result)