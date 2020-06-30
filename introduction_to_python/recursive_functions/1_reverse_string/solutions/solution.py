# Write your solution here
def reverse(string):
    if string=="":
        return ""
    return string[-1]+reverse(string[0:len(string)-1])