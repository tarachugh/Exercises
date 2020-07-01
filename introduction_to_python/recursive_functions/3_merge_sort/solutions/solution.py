# Write your solution here
def custom_sort(num_list):
    length=len(num_list)
    if length<2:
        return(num_list)
    L=num_list[0:(length//2)]
    R=num_list[(length//2):]
    custom_sort(L)
    custom_sort(R)
    combine(L, R, num_list)
    return num_list


def combine(L, R, num_list):
    lenL=len(L)
    lenR=len(R)
    a=0
    b=0
    c=0
    while(a<lenL and b<lenR):
        if L[a]<=R[b]:
            num_list[c]=L[a]
            a+=1
        else:
            num_list[c]=R[b]
            b+=1
        c+=1
    while a<lenL:
        num_list[c]=L[a]
        a+=1
        c+=1
    while b<lenR:
        num_list[c]=R[b]
        b+=1
        c+=1

print(custom_sort([1,7,4,2]))