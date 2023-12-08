"""
Program: classes.py
Author: Logan Kennebeck
Last date modified: 12/1/2023

Contains the extra classes needed for the expense tracker
"""
def insertion_sort(queue):
    size = len(queue.items)

    if size <= 1:
        return

    for i in range(1, size):
        key = queue.items[i]
        j = i - 1
        while j >= 0 and float(key.amount) < float(queue.items[j].amount):
            queue.items[j + 1] = queue.items[j]
            j -= 1
        queue.items[j + 1] = key

class Expense:
    def __init__(self, company, item_type, amount):
        self.company = company
        self.item_type = item_type
        self.amount = amount

class Month:
    def __init__(self, month, expenses):
        self.month = month
        self.expenses = expenses

class Node:
    def __init__(self, item = None, next=None):
        self.item = item
        self.next = next

class LinkedList:
    #constructor
    def __init__(self):
        self.head = None
        self.length = 0

    #returns true if length is 0, else false
    def is_empty(self):
        return self.length == 0

    # inserting a new item into the list
    def insert(self, item):
        self.length += 1
        new_node = Node(item)
        if(self.head):
            current = self.head
            # making sure we are adding the next list item to the back of the list
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            # if head = None (empty list) we add the item to the front of the list
            self.head = new_node

    def replace(self, old_item, new_item):
        if not self.is_empty():
            current = self.head

            while current:
                if old_item == current.item:
                    break
                current = current.next
            current.item = new_item
            return

    # removing a specific item from the list
    def remove(self, item):
        # checking if list is empty
        if not self.is_empty():
            current = self.head

            # checking if the item to remove is at the start of the list
            # and removing the item and updating the head node
            if current.item == item:
                self.head = current.next
                current = None
                self.length -= 1
                return

            # cycling through the list to find the item
            while current:
                # returning a string if the item is not in the list
                if current.item != item and current.next == None:
                    error_str = 'Item not found'
                    return error_str

                #exiting the loop when the item is found
                if item == current.item:
                    break
                prev = current
                current = current.next

            # updating the list and removing the node and changing the previous node
            # so that is correctly points to the next list item
            prev.next = current.next
            self.length -= 1
            return

    # displaying the items in the list for the user
    def print(self):
        #checking if the list is empty
        if not self.is_empty():
            list_str = ''
            current = self.head
            # looping through and appending each item to the list
            while(current):
                list_str += f'{current.item}\n'
                current = current.next
            return list_str

    # returning the size of the list for the user
    def size(self):
        return self.length

class Queue:
    def __init__(self):
        self.head = -1
        self.tail = -1
        self.length = 0
        self.items = []  # holds each element in the queue, reserving spaces for empty slots

    def is_empty(self):
        # returns true if length is equal to 0, otherwise returns false
        return self.length == 0

    def enqueue(self, item):
        # adds items to the back of the queue (index represented by the self.tail variable)
        # self.tail calue increments by one and self.head value increases by one if the queue was previously empty
        if self.is_empty():
            self.head += 1
        self.items.append('')
        self.tail += 1
        self.items[self.tail] = item
        self.length += 1
        return

    def dequeue(self):
        # removes item from the front of the queue (index represented by the self.head variable)
        # self.tail value decrements by one and self.head value decreases by one if the queue becomes empty
        if not self.is_empty():
            item_str = self.items.pop(self.head)
            self.tail -= self.tail
            self.length -= 1
            if self.length == 0:
                self.head -= 1
            return item_str

    def peek(self):
        # look at front item in the queue without removing
        if not self.is_empty():
            item_str = self.items[self.head]
            return item_str
        raise QueueEmptyException('Queue is empty!')

    def size(self): # get queue size or length
        return self.length

    def print_queue(self):
        # appends each item in the queue to a string to display them
        if not self.is_empty():
            stack_str = ""
            for x in range(len(self.items)):
                stack_str += f'{self.items[x]}\n'
            return stack_str;
