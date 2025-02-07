# TASK:
#
# Write a random tester for the Queue class.
# The random tester should repeatedly call 
# the Queue methods on random input in a 
# semi-random fashion. for instance, if 
# you wanted to randomly decide between 
# calling enqueue and dequeue, you would 
# write something like this:
#
# q = Queue(500)
# if (random.random() < 0.5):
#     q.enqueue(some_random_input)
# else:
#     q.dequeue()
#
# You should call the enqueue, dequeue, 
# and checkRep methods several thousand 
# times each.

import array
import random

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)

# Write a random tester for the Queue class.
def test():
    
    #Create a queue of random size
    size = random.randint(1,50)
    q = Queue(size)

    # Make sure queue is empty
    isEmpty = q.empty()
    assert (isEmpty == True)
    # List with all elements of queue
    inputList = []

    for x in range (100000):
        
        q.checkRep()

        # Generate random number
        number = random.randint(-100000, 1000000)

        # Randomly choose between enqueue or dequeue
        if (random.random() < 0.5):
            # Try to enqueue
            if (q.enqueue(number) == True):
                inputList.append(number)
        
        else:
            # Check that dequeue worked
            if (q.dequeue() != None):
                # Remove first item of list
                inputList.pop(0)
        q.checkRep()
        
        # Check if list is empty
        if len(inputList) == 0:
            assert q.empty() == True

        # Check if list is full
        elif len(inputList) == size:
            assert q.full() == True

        q.checkRep()


test()

