from Queue import CircularQueue

q = CircularQueue()
for i in range(8):
    q.enqueue(i)
q.display()

for i in range(5):
    q.dequeue()
q.display()

for i in range(8, 14):
    q.enqueue(i)
q.display()