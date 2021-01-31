class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# Implement stack data structure using queue

class Stack:
    def __init__(self):
        # Write your definition for __init__ here
        self.q1 = Queue()
        self.q2 = Queue()

        self.cur_size = 0
        return

    def isEmpty(self):
        return self.cur_size == 0

    def push(self, item):
        self.cur_size += 1
        self.q2.enqueue(item)

        while not self.q1.isEmpty():
            self.q2.enqueue(self.q1.dequeue())

        self.q1, self.q2 = self.q2, self.q1
        return

    def pop(self):
        if self.q1.isEmpty():
            return
        self.cur_size -= 1
        return self.q1.dequeue()

    def peek(self):
        if self.q1.isEmpty():
            return None
        value = self.pop()
        self.push(value)
        return value

    def size(self):
        # Write your definition for size here
        return self.cur_size


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    pop1 = stack.pop()
    size1 = stack.size()
    stack.push(4)
    pop2 = stack.pop()
    size2 = stack.size()
    peek2 = stack.peek()
    pop3 = stack.pop()
    size3 = stack.size()
    stack.push(5)
    pop4 = stack.pop()
    size4 = stack.size()

    print(f"pop1: {pop1}, size1: {size1}")
    print(f"pop2: {pop2}, size2: {size2}, peak2: {peek2}")
    print(f"pop3: {pop3}, size3: {size3}")
    print(f"pop4: {pop4}, size4: {size4}")


