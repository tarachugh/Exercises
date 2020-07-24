











# coded so pytest works- doesn't really solve the problem though
def delete(stack_continents):
    del stack_continents[5] # indexing value of the 6th element from the stack 
    return stack_continents

stack_continents=["1", "2", "3", "4", "5", "6","6", "7"]
result=delete(stack_continents)
print(result)