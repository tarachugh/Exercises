import queue
def create_queue():
    queue_a=queue.Queue(maxsize=5)
    queue_a.put(1)
    queue_a.put(2)
    queue_a.put(3)
    queue_a.put(4)
    queue_a.put(5)
    return queue_a

data=create_queue()
data=list(data.queue)
for i in data:
    print(i)

# Queue class is a class inside the module queue