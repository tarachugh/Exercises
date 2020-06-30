# Write your solution here
def count_ways(n):
    if n==1 or n==0:
        return 1
    return count_ways(n-1)+count_ways(n-2)
    