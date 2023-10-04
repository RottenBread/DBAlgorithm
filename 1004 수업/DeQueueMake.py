from Dequeue import *

dq = CircularDeque()
for i in range(9):
    if i % 2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)
dq.display()

for i in range(2):
    dq.deleteFront()

for i in range(3):
    dq.deleteRear()
dq.display()

for i in range(9, 14):
    dq.addFront(i)
dq.display()
