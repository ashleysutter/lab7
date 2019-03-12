# CPE 202 lab 7
# Name: Ashley Sutter
# Student ID: 011278952
# Date (last modified): 2/27/2019
#
# Lab 7
# Section 5
# Purpose: Create a heap
# additional comments

class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.capacity = capacity
        self.heap = [None] * (capacity + 1)
        self.size = 0

    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""
        if self.is_full():
            return False
        else:
            self.size += 1
            i = self.size
            self.heap[i] = item
            self.perc_up(i)
            return True

    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        return self.heap[1]


    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.is_empty():
            return None
        else:
            max_item = self.heap[1]
            i = self.size
            self.heap[1] = self.heap[i]
            self.heap[i] = None
            self.perc_down(1)
            self.size -= 1
            return max_item

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        contents = []
        for i in range(1, self.get_size() + 1):
            contents.append(self.heap[i])
        return contents

    def build_heap(self, alist):
        """Builds a heap from the items in alist and builds a heap using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased"""
        length = len(alist)
        if self.capacity < length:
            self.heap = self.heap + ([None] * (length - self.capacity))
            self.capacity = length
        for item in alist:
            self.enqueue(item)

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        return True if self.size == 0 else False

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        return True if self.size == self.capacity else False
        
    def get_capacity(self):
        """this is the maximum number of entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.capacity
    
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.size
        
    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        left_child_index = self.get_left_child_index(i) 
        right_child_index = self.get_right_child_index(i)
        max_index = i
        size = self.get_size()
        if left_child_index < size and (self.heap[left_child_index] > self.heap[max_index]):
            max_index = left_child_index
        if right_child_index < size and (self.heap[right_child_index] > self.heap[max_index]):
            max_index = right_child_index
        if max_index != i:
            self.swap(max_index, i)
            self.perc_down(max_index)
        
    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        parent_index = self.get_parent_index(i)
        if self.heap[parent_index] < self.heap[i]:
            self.swap(parent_index, i)
            self.perc_up(parent_index)

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order"""
        length = len(alist)
        self = MaxHeap(length)
        self.build_heap(alist)
        for i in range(length - 1, -1, -1):
            alist[i] = self.dequeue()

    def get_parent_index(self, i):
        if i == 1:
            return 1
        elif i % 2 == 0:
            return i // 2
        else: 
            return (i - 1) // 2

    def get_left_child_index(self, i):
        return i * 2

    def get_right_child_index(self, i):
        return (i*2)+1

    def swap(self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp
