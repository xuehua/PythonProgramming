# Problem 1. Implement a Stack Using Queues 
https://leetcode.com/problems/implement-stack-using-queues/


    class Queue:
        def __init__(self):
            self.items = []

        def empty(self):
            return self.items == []

        def enqueue(self, item):
            self.items.insert(0, item)

        def dequeue(self):
            return self.items.pop()

        def size(self):
            return len(self.items)

Please complete the following Stack class using the API of the Queues. 
    class Stack:
        def __init__(self):
            # Write your definition for __init__ here
            return

        def isEmpty(self):
            # Write your definition for isEmpty here
            return

        def push(self, item):
            # Write your definition for push here
            return

        def pop(self):
            # Write your definition for pop here
            return

        def peek(self):
            # Write your definition for peek here
            return

        def size(self):
            # Write your definition for size here
            return
