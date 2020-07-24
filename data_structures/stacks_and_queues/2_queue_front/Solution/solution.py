import queue

def queue_a():
    queue_a=queue.Queue(maxsize=5)
    queue_a.put(1)
    queue_a.put(2)
    queue_a.put(3)
    queue_a.put(4)
    queue_a.put(5)
    return queue_a.get()
    # queue.get () returns head value in queue

result=queue_a()
print(result)

# could also have cast queue to list and returned index 1
