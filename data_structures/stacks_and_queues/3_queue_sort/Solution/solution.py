import queue
q=queue.Queue(maxsize=5)
q.put(3)
q.put(4)
q.put(2)
q.put(5)
q.put(1)


def min(q, last_index):
    newq=q
    smallest=q.get()
    for i in range(last_index+1):
        a=q.get()
        if a>=smallest:
            smallest=a
    return smallest

def mintorear(q, minimum):
    q.put(minimum)
    return q

def sort(q, last_index):
    a= min(q,last_index)
    qnew=mintorear(q,a)
    if last_index>=0:
        sort(qnew, last_index-1)
    return qnew


a= sort(q, 4)
print(list(a.queue))
