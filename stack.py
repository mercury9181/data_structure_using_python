class Empty(Exception):
    pass

class array_stack:
    def __init__(self):
        self.data = list()
    def _len(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0
    def push(self,element):
        return self.data.append(element)
    def pop(self):
        if self.is_empty():
            raise Empty("Empty stack")
        return self.data.pop()
    def top(self):
        if self.is_empty():
            raise Empty("Empty stack")
        return self.data[-1]

s= array_stack()
s.push(10)
s.push(20)
s.push(40)
print("stack: ", s.data)
print("Length of stack: ", s._len())
print("is the stack empty: ", s.is_empty())
s.pop()
print("stack: ", s.data)
print("Length of stack: ", s._len())
print("is the stack empty: ", s.is_empty())
print("is the stack empty: ", s.is_empty())
s.pop()
print("stack: ", s.data)
print("Length of stack: ", s._len())
s.pop()
print("stack: ", s.data)
print("Length of stack: ", s._len())
print("is the stack empty: ", s.is_empty())
