

class Empty(Exception):
    pass


class linked_stack:
    class node:
        __slots__ = 'element','next'

        def __init__(self,element,next):
            self.element = element
            self.next = next
    
    def __init__(self):
        self.head = None
        self.size = 0

    def len(self):
        return self.size
    def is_empty(self):
        return self.size==0
    



    def push(self,element):
        self.head = self.node(element,self.head)
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise Empty("stack is empty")
        value = self.head.element
        self.head = self.head.next
        self.size -= 1
        return value
    
    def top(self):
        if self.is_empty():
            raise Empty("stack is empty")
        return self.head.element

    def display(self):
        temp = self.head
        while temp:
            print(temp.element, end="-->")
            temp = temp.next
        print()

ls = linked_stack()

ls.push(10)
ls.display()
ls.push(20)
ls.display()

ls.pop()
ls.display()









