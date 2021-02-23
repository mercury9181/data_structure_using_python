class Empty(Exception):
    pass

class array_dqueue:
    def __init__(self):
        self.data = list()
        # self.size = 0
        self.front = 0
    def array_size(self):
        a= len(self.data)
        return a
    def is_empty(self):
        return len(self.data)==0
    def add_first(self,element):
        self.data.insert(self.front,element)
    def add_last(self,element):
        self.data.append(element)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data.pop(0)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data.pop()        
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front]



 

s= array_dqueue()
s.add_first(60)
s.add_first(30)
s.add_first(10)
print("queue: ", s.data)
s.add_first(20)
print("queue: ", s.data)
s.add_last(40)
print("queue: ", s.data)
print("Length of dqueue: ", s.array_size())
print("is the dqueue empty: ", s.is_empty())


s.delete_first()
print("queue: ", s.data)
s.delete_last()
print("queue: ", s.data)
print("Length of dqueue: ", s.array_size())
print("is the dqueue empty: ", s.is_empty())