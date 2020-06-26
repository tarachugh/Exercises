# Code your solution here
line=input()
y=line.split()
z="".join(y)
z=z.lower()
print(z)
if(z==z[::-1]):
    is_palindrome= True
else:
    is_palindrome= False

print(is_palindrome)
