# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently 
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold 
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which 
#    should be 10
#
# Your test function should run assertion checks and throw an 
# AssertionError for each of the 5 incorrect Queues. Pressing 
# submit will tell you how many you successfully catch so far.


from queue_test import *

def test():
    
    # Create a queue of small size
    q = Queue(2)

    # Enqueue a very large element
    success = q.enqueue(1000000000)

    # Make sure that adding element in queue worked
    assert success

    # Make sure that queue is not empty
    assert not q.empty()

    # Get element from the queue
    value = q.dequeue()

    # Make sure element is the same as the element enqueued
    assert value == 1000000000

    # Try to get another element from the queue
    value = q.dequeue()

    # Make sure queue is empty
    assert q.empty()

    # Make sure we got nothing since queue should be empty now
    assert value == None

    # Make sure queue is empty again
    assert q.empty()
    
    # Create a queue of size 100 (bigger this time)
    q = Queue(100)

    # Loop to fill the queue 
    for i in range(100):

        #Add element to queue
        success = q.enqueue(i)
        
        # Make sure every element was added correctly
        assert success
     
    


