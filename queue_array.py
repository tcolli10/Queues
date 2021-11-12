
from logging import captureWarnings


class Queue:
    '''Implements an array-based, efficient first-in first-out Queue Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.head = 0
        self.items = [None] * capacity
        self.capacity = capacity
        self.num_items = 0


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == 0:
            return True
        else:
            return False


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == self.capacity:
            return True
        else:
            return False


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            self.items[0] = item
            self.num_items += 1
        elif self.is_full():
            raise IndexError
        else:
            index = (self.head + self.num_items) % self.capacity
            self.items[index] = item
            self.num_items += 1

            


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        else:
            returnValue = self.items[self.head]
            self.head += 1 
            self.num_items -= 1
        return returnValue



    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items

