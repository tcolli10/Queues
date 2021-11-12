
class Node:
    def __init__(self,item):
        self.data = item
        self.next = None

class Queue:
    '''Implements an linked list based ,efficient first-in first-out Queue Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.tail = None
        self.head = None
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
        new_node = Node(item)
        if self.is_full():
            raise IndexError
        elif self.is_empty():
            self.head = new_node
            self.tail = self.head
            self.num_items += 1
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
            self.num_items += 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        else:
            returnValue = self.head.data
            self.head = self.head.next
            self.num_items -= 1
        return returnValue

        


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items
    


