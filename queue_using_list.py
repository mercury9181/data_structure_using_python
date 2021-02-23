class Empty(Exception):
    pass

class array_queue:
    def __init__(self):
        self.data = list()
        # self.size = 0
        self.front = 0
    def array_size(self):
        a= len(self.data)
        return a
    def is_empty(self):
        return len(self.data)==0
    def enqueue(self,element):
        self.data.append(element)

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data.pop(0)
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front]



 

s= array_queue()
s.enqueue(10)
s.enqueue(20)
s.enqueue(40)

print("queue: ", s.data)
print("Length of queue: ", s.array_size())
print("is the queue empty: ", s.is_empty())
s.dequeue()
print("queue: ", s.data)
print("Length of queue: ", s.array_size())
print("is the queue empty: ", s.is_empty())
print("first element: ", s.first())
s.dequeue()
print("queue: ", s.data)
print("Length of queue: ", s.array_size())
print("is the queue empty: ", s.is_empty())
print("first element: ", s.first())