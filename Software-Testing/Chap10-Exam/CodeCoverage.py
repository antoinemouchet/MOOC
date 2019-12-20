# Code Coverage
# ---------------
# Achieve full statement coverage and parameter value coverage for
# strings, integers, and booleans on this enhanced Queue class.
#
# You will need to:
# 1) Write your test code in the test function.
# 2) Press submit. The grader will tell you if you 
#    fail to cover any specific part of the code.
# 3) Update your test function until you cover the 
#    entire code base.

# This specific Queue class can enqueue not only integers,
# but strings and booleans as well. You will need to provide
# parameter value coverage for these data types by adding
# each type of data into your Queue. 
#
# Furthermore, this Queue class has the additional methods
# clear() and enqueueall(). The enqueueall method takes
# in a list or tuple and enqueues each item of the collection
# individually, returning True if all enqueues succeed, and
# False if the number of items in the collection will overfill
# the Queue.


# Enhanced Queue class
class Queue:
    
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = {}

    def __str__(self):
        return str(self.data)

    def clear(self):       
        self.__init__(self.max)

    def empty(self):       
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if type(x) is not int and type(x) is not str and type(x) is not bool:
            return False
        if self.size == self.max:
            return False
        
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:           
            self.tail = 0
        return True

    def enqueueall(self, c):
        if type(c) is tuple or type(c) is list:
            if not self.size + len(c) > self.max:
                for itm in c:
                    self.enqueue(itm)
                return True
        return False

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


# Provide full statement and parameter value coverage of the Queue class
def test():
    # Define a dico {type : list of values of type}
    # Type can be bool, str or int following spec
    values = {"bool": [True, False],
              "str": ["Hello", "Test", "Lore ipsum", "World", "Cinq"],
              "int": [1, 5, 50000, 645, 23, 42]}
    
    # Create a queue and call the sanity check on it
    q = Queue(5)
    q.checkRep()

    # Should be empty
    assert q.empty()

    # --- Invalid testing --
    # Enqueue invalid type
    success = q.enqueue(2.5)
    assert not success

    #Enqueue all invalid type
    success = q.enqueueall(2.50)
    assert not success
    
    # Queue should still be empty
    assert q.empty()

    # Dequeue on empty list
    value = q.dequeue()
    assert value == None
    # -- End of invalid testing --


    # Loop on all the valid types
    for enqueueType in values.keys():

        # Enqueue all elements of type
        success = q.enqueueall(values[enqueueType])
        q.checkRep()
        
        # More items than size of queue
        if enqueueType == "int":
            assert not success
    
        else:
            assert success
        
        # 5 strings is as much as allowed by a queue of 5
        if enqueueType == "str":
            assert q.full()

        # Clear the queue    
        q.clear()
        q.checkRep()
        assert q.empty()

        # Loop to enqueue all items of type
        for item in values[enqueueType]:
            success = q.enqueue(item)
            q.checkRep()

            # Check if index can be inside the queue
            if values[enqueueType].index(item) >= 5:
                assert q.full()
                assert not success


        # Loop to dequeue item until queue is empty
        while not q.empty():
           value = q.dequeue()
           q.checkRep()
           # A value should be returned.
           assert value != None
        
        # Clear the queue when type totally tested
        q.clear()
        q.checkRep()
    
    # Get data of queue
    data = q.__str__()
    #print(data)

test()
