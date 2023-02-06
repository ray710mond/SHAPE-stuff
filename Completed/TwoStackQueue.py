class TwoStackQueue:
    def __init__(self):
        self.instack = [] # add an item to this stack
        self.outstack = [] # pop an item out of this stack
    def enqueue(self, item):
        # TODO - add an item to the queue
        self.instack.append(item)
    def dequeue(self):
        # TODO - remove an from the front of the queue
        try:
            if not self.outstack:
                while self.instack:
                    self.outstack.append(self.instack.pop())
            return self.outstack.pop()
        except IndexError:
           print("The queue is already empty!")

q = TwoStackQueue()

q.enqueue("C")
q.enqueue(2)
q.enqueue("A")

print(q.dequeue()) # print C
print(q.dequeue()) # print 2
print(q.dequeue()) # print A

q2 = TwoStackQueue()
print(q.dequeue()) # should not be an error!

