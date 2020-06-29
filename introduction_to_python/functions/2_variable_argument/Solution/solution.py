# Code your solution here
def var_arg(*args):
    result=""
    for i in args:
        result+=i
    return result

result=var_arg("Hi ", "I ", "am ", "Tara")
print(result)